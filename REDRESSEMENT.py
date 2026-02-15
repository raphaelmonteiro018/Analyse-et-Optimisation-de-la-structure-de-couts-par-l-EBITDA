import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement des données
try:
    df = pd.read_excel('pnl_ready_for_mlr.xlsx')
except FileNotFoundError:
    print("Erreur : Le fichier 'pnl_ready_for_mlr.xlsx' est introuvable.")
    exit()

# --- CONFIGURATION DU PLAN DE REDRESSEMENT FINAL ---
# 1. Coefficient d'élasticité issu de la régression OLS (Impact pour 1.0 de variation)
coef_margin = 2671.72

# 2. Stratégie de coupes budgétaires différenciées
reductions = {
    'Cost_Rent': 0.25,      # Critique (|beta| > 1.0)
    'Cost_Sales': 0.25,     # Critique (|beta| > 1.0)
    'Cost_Marketing': 0.15,
    'Cost_Admin': 0.15,
    'Cost_IT': 0.10,        # Efficient - On préserve
    'Cost_HR': 0.10
}

# 3. Levier de Valeur (Le "What-if" : Gain de 0.5 point de marge brute)
# On exprime 0.5% en valeur décimale pour le calcul statistique
choc_marge_points = 0.5
choc_marge_decimal = choc_marge_points / 100 

# 2. Analyse par branche
print("--- 🚀 FEUILLE DE ROUTE OPÉRATIONNELLE : SCÉNARIO DE RENTABILITÉ FINALE ---")
print(f"Stratégie : Coupes différenciées & Choc de valeur (+{choc_marge_points}pt marge)\n")

cost_cols = list(reductions.keys())
metrics_cols = ['Gross_Margin_Rate', 'Sales', 'EBITDA', 'Cost_Rent', 'Cost_Sales']
branch_summary = df.groupby('Branch')[list(set(cost_cols + metrics_cols))].mean()

plan_data = []

for branch, row in branch_summary.iterrows():
    # --- CALCUL DES GAINS ---
    
    # A. Gain par optimisation des coûts
    gain_ope = sum([row[col] * red for col, red in reductions.items()])
    
    # B. Gain par choc de valeur (Coefficient * Variation en points de taux)
    # On multiplie le coefficient de sensibilité par la variation de 0.005
    gain_valeur = coef_margin * choc_marge_decimal
    
    ebitda_projete = row['EBITDA'] + gain_ope + gain_valeur
    
    # --- DIAGNOSTIC BUSINESS ---
    if row['Cost_Rent'] > branch_summary['Cost_Rent'].mean():
        status_rent = "🔴 SURÉVALUÉ (Renégociation prioritaire)"
    else:
        status_rent = "🟢 Aligné"
        
    efficiency = row['Sales'] / row['Cost_Sales']
    avg_efficiency = branch_summary['Sales'].mean() / branch_summary['Cost_Sales'].mean()
    
    if efficiency < avg_efficiency:
        status_sales = f"⚠️ SOUS-PERFORMANT ({efficiency:.2f} € CA/€)"
    else:
        status_sales = f"✅ EFFICIENT ({efficiency:.2f} € CA/€)"

    # --- AFFICHAGE DES RÉSULTATS ---
    print(f"📍 RÉGION : {branch}")
    print(f"    Actuel : EBITDA {row['EBITDA']:,.2f} €")
    
    verdict = "🟢 RENTABLE" if ebitda_projete > 0 else "🔴 TOUJOURS DÉFICITAIRE"
    print(f"    📈 IMPACT PROJETÉ : {ebitda_projete:,.2f} € | Statut : {verdict}")
    print(f"      (Détail Gain : Coûts +{gain_ope:,.2f}€ | Valeur +{gain_valeur:,.2f}€)")
    print(f"    👉 Immo : {status_rent} | Force de Vente : {status_sales}")
    print("-" * 75)

    plan_data.append({
        'Branch': branch,
        'EBITDA_Initial': row['EBITDA'],
        'EBITDA_Projete': ebitda_projete,
        'Gain_Total': gain_ope + gain_valeur,
        'Part_Optimisation_Couts': gain_ope,
        'Part_Gain_Valeur': gain_valeur,
        'Verdict': verdict
    })

# 3. Exportation Finale
pd.DataFrame(plan_data).to_excel('plan_redressement_PRO_RENTABLE.xlsx', index=False)
print("\n✅ Analyse terminée. Le plan de rentabilité a été exporté sous : 'plan_redressement_PRO_RENTABLE.xlsx'")

# --- VISUALISATION ---
plot_df = pd.DataFrame(plan_data).melt(
    id_vars='Branch', 
    value_vars=['EBITDA_Initial', 'EBITDA_Projete'], 
    var_name='Scenario', 
    value_name='EBITDA'
)

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
colors = {"EBITDA_Initial": "#e74c3c", "EBITDA_Projete": "#27ae60"}
ax = sns.barplot(data=plot_df, x='Branch', y='EBITDA', hue='Scenario', palette=colors)
plt.axhline(0, color='black', linewidth=1.5, linestyle='--')
plt.title("🚀 Impact du Plan de Redressement : Retour à la Rentabilité", fontsize=14, fontweight='bold')
plt.ylabel("EBITDA Hebdomadaire (€)")

for p in ax.patches:
    if p.get_height() != 0:
        ax.annotate(f'{p.get_height():.0f}€', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 9 if p.get_height() > 0 else -9), 
                    textcoords='offset points', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('ebitda_comparison.png')
plt.show()

# Waterfall pour la branche North-01
target_branch = plan_data[1] 
labels = ['Initial', 'Gain Coûts', 'Gain Marge', 'Final']
values = [
    target_branch['EBITDA_Initial'], 
    target_branch['Part_Optimisation_Couts'], 
    target_branch['Part_Gain_Valeur'], 
    target_branch['EBITDA_Projete']
]

plt.figure(figsize=(10, 6))
colors_wf = ['#e74c3c', '#3498db', '#f1c40f', '#27ae60']
plt.bar(labels, values, color=colors_wf)
plt.title(f"💡 Décomposition de la Performance : {target_branch['Branch']}", fontsize=12)
plt.ylabel("Impact (€)")
plt.tight_layout()
plt.savefig('waterfall_logic.png')
plt.show()