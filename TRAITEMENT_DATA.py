import pandas as pd
import numpy as np

# =============================================================================
# 1. CONFIGURATION ET PARAMÉTRAGE DES FLUX
# =============================================================================
# Fichier source : Données comptables brutes (ERP/Gestion)
# Fichier cible : Dataset structuré pour la modélisation économétrique
input_file = 'pnl_source.xlsx'
output_file = 'pnl_ready_for_mlr.xlsx'

try:
    # Chargement des données transactionnelles (Ventes) et structurelles (Charges)
    orders = pd.read_excel(input_file, sheet_name='Orders')
    opex_real = pd.read_excel(input_file, sheet_name='OPEX_Monthly')

    print("Initialisation du pipeline : Consolidation des Revenus, Volumes et Indicateurs de Rentabilité...")

    # =============================================================================
    # 2. ÉTAPE A : TRAITEMENT DES REVENUS ET VOLUMES TRANSACTIONNELS
    # =============================================================================
    # Calcul du coût des ventes (COGS) analytique
    orders['COGS_Clean'] = orders['Quantity'] * orders['UnitCost']
    orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])
    
    # Agrégation hebdomadaire par Business Unit pour l'analyse de série temporelle
    actuals_hebdo = orders.groupby(['Branch', pd.Grouper(key='OrderDate', freq='W-SUN')]).agg({
        'Sales': 'sum', 
        'COGS_Clean': 'sum',
        'Quantity': 'sum'  # Mesure du volume d'activité pour l'analyse d'élasticité
    }).reset_index().rename(columns={'OrderDate': 'Date'})

    # =============================================================================
    # 3. ÉTAPE B : VENTILATION ET LINÉARISATION DES CHARGES FIXES (OPEX)
    # =============================================================================
    def to_weekly_detailed(df):
        """
        Transforme les charges mensuelles en flux quotidiens linéarisés 
        pour une ré-agrégation hebdomadaire précise.
        """
        df['Date_Start'] = pd.to_datetime(df['Month'].astype(str) + '-01')
        df['Days_in_Month'] = df['Date_Start'].dt.days_in_month
        
        rows = []
        for _, r in df.iterrows():
            daily_amt = r['OPEX_Amount'] / r['Days_in_Month']
            for d in range(r['Days_in_Month']):
                day = r['Date_Start'] + pd.Timedelta(days=d)
                rows.append({
                    'Branch': r['Branch'], 
                    'Dept_Name': r['Department'], 
                    'Date': day, 
                    'Amount': daily_amt
                })
        return pd.DataFrame(rows)

    # Exécution de la linéarisation temporelle
    opex_daily = to_weekly_detailed(opex_real)
    
    # Reconstruction hebdomadaire et pivotement par centre de profit
    opex_hebdo = opex_daily.groupby(['Branch', 'Dept_Name', pd.Grouper(key='Date', freq='W-SUN')])['Amount'].sum().reset_index()
    opex_pivot = opex_hebdo.pivot(index=['Branch', 'Date'], columns='Dept_Name', values='Amount').reset_index().fillna(0)
    
    # Nomenclature des colonnes : Préfixe 'Cost_' pour l'identification des features de régression
    dept_list = [c for c in opex_pivot.columns if c not in ['Branch', 'Date']]
    opex_pivot = opex_pivot.rename(columns={c: f"Cost_{c}" for c in dept_list})
    
    # Agrégation de la structure de coûts totale (Total OPEX)
    cost_cols = [f"Cost_{c}" for c in dept_list]
    opex_pivot['OPEX_Total'] = opex_pivot[cost_cols].sum(axis=1)

    # =============================================================================
    # 4. ÉTAPE C : FUSION ANALYTIQUE ET CALCUL DES INDICATEURS DE PERFORMANCE
    # =============================================================================
    # Jointure des flux de revenus et de charges pour obtenir le P&L hebdomadaire
    df_mlr = pd.merge(actuals_hebdo, opex_pivot, on=['Branch', 'Date'], how='left').fillna(0)

    # 1. Calcul de l'EBITDA (Excédent Brut d'Exploitation)
    df_mlr['EBITDA'] = (df_mlr['Sales'] - df_mlr['COGS_Clean']) - df_mlr['OPEX_Total']
    
    # 2. Calcul du Taux de Marge Brute (Variable clé de sensibilité)
    df_mlr['Gross_Margin_Rate'] = np.where(df_mlr['Sales'] > 0, 
                                           (df_mlr['Sales'] - df_mlr['COGS_Clean']) / df_mlr['Sales'], 
                                           0)

    # 3. Calcul du Point Mort (Break-Even Sales en valeur)
    # Détermine le niveau de chiffre d'affaires requis pour couvrir les charges fixes
    df_mlr['BreakEven_Sales'] = np.where(df_mlr['Gross_Margin_Rate'] > 0,
                                         df_mlr['OPEX_Total'] / df_mlr['Gross_Margin_Rate'],
                                         0)

    # 4. Calcul du Prix Unitaire Moyen (Analyse de la contribution par unité)
    df_mlr['Avg_Unit_Price'] = np.where(df_mlr['Quantity'] > 0, df_mlr['Sales'] / df_mlr['Quantity'], 0)

    # =============================================================================
    # 5. EXPORT ET VALIDATION DU DATASET PRÊT POUR LE MACHINE LEARNING
    # =============================================================================
    df_mlr.to_excel(output_file, index=False)
    
    print(f"✅ Pipeline ETL terminé. Dataset généré : {output_file}")
    print(f"Métriques consolidées : Ventes, Volumes, Point Mort, EBITDA.")

except Exception as e:
    print(f"❌ Erreur critique lors du traitement : {e}")