import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages 

# =============================================================================
# 1. CHARGEMENT ET PRÉPARATION DU DATASET ANALYTIQUE
# =============================================================================
# Extraction du P&L retraité pour la modélisation économétrique
try:
    df = pd.read_excel('pnl_ready_for_mlr.xlsx')
except FileNotFoundError:
    print("Erreur : Fichier source 'pnl_ready_for_mlr.xlsx' introuvable.")
    exit()

# =============================================================================
# 2. SPÉCIFICATION DU MODÈLE ET VARIABLES EXPLICATIVES
# =============================================================================
# Isolation des leviers de revenus et des centres de coûts (OPEX)
cost_features = [c for c in df.columns if c.startswith('Cost_')]
features = ['Sales', 'Gross_Margin_Rate'] + cost_features

# Définition de la matrice des prédicteurs (X) avec ajout d'une constante (Intercept)
X = df[features]
X = sm.add_constant(X)

# Définition de la variable cible (Y) : Performance opérationnelle (EBITDA)
Y = df['EBITDA']

# =============================================================================
# 3. ESTIMATION PAR LA MÉTHODE DES MOINDRES CARRÉS ORDINAIRES (OLS)
# =============================================================================
# Calcul des coefficients de régression et des statistiques de robustesse
model = sm.OLS(Y, X).fit()

# =============================================================================
# 4. GÉNÉRATION DU RAPPORT DE DIAGNOSTIC (EXPORT PDF)
# =============================================================================
with PdfPages('Diagnostic_MLR_EBITDA.pdf') as pdf:
    
    # --- PAGE 1 : MATRICE DE CORRÉLATION ET MULTICOLINÉARITÉ ---
    # Évaluation des interdépendances entre les leviers et la rentabilité
    plt.figure(figsize=(12, 10))
    corr_matrix = df[features + ['EBITDA']].corr()
    
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        fmt=".4f", 
        cmap='RdBu_r', 
        center=0,
        linewidths=1, 
        linecolor='black', 
        cbar_kws={"label": "Coefficient de Corrélation"}
    )
    
    plt.title('MATRICE DE CORRÉLATION : DIAGNOSTIC MULTIDIMENSIONNEL DES LEVIERS', fontsize=14, fontweight='bold', pad=20)
    plt.xticks(fontweight='bold', rotation=45, ha='right')
    plt.yticks(fontweight='bold')
    
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # --- PAGE 2 : ANALYSE DES RÉSIDUS (QUALITÉ DE LA PRÉDICTION) ---
    # Vérification de la normalité des erreurs pour valider la robustesse du modèle
    plt.figure(figsize=(10, 6))
    sns.histplot(model.resid, kde=True, color='skyblue', stat="density", linewidth=0)
    plt.axvline(x=0, color='red', linestyle='--', label='Biais Nul (E(ε) = 0)')
    
    plt.title('DISTRIBUTION DES RÉSIDUS : VALIDATION DU MODÈLE', fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Écarts de Prédiction (Erreurs Modèle)', fontsize=11, fontweight='bold')
    plt.ylabel('Densité de Probabilité', fontsize=11, fontweight='bold')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('04_Distribution_Residus_Simple.png', dpi=300)
    pdf.savefig() 
    plt.close()

    # --- PAGE 3 : HIÉRARCHIE DE L'IMPACT MARGINAL (COEFFICIENTS) ---
    # Identification des coûts "Toxiques" (levier > |1.0|) vs "Efficients"
    coef_df = model.params.drop('const').sort_values()
    plt.figure(figsize=(10, 8))
    
    # Codage couleur : Rouge pour destruction de valeur nette, Bleu pour support opérationnel
    colors = ['#e74c3c' if x < -1 else '#3498db' for x in coef_df] 
    
    coef_df.plot(kind='barh', color=colors, edgecolor='black')
    plt.axvline(x=-1, color='black', linestyle='--', label='Seuil de Toxicité (Impact > 1:1)')
    
    plt.title('SENSIBILITÉ MARGINALE DE L\'EBITDA (COEFFICIENTS BETA)', fontsize=12, fontweight='bold')
    plt.xlabel('Impact Unitaire sur l\'EBITDA (€)', fontweight='bold')
    plt.legend()
    plt.tight_layout()
    pdf.savefig()
    plt.close()

# =============================================================================
# 5. SYNTHÈSE DES RÉSULTATS DANS LA CONSOLE
# =============================================================================
print("\n" + "="*60)
print("📊 RAPPORT ÉCONOMÉTRIQUE GÉNÉRÉ")
print(f"📁 PDF : Diagnostic_MLR_EBITDA.pdf")
print(f"📁 PNG : 04_Distribution_Residus_Simple.png")
print("="*60)

print("\n--- SYNTHÈSE DES COEFFICIENTS ET STATISTIQUES DE RÉGRESSION ---")
# Affichage du résumé statistique complet (R², P-values, F-stat)
print(model.summary())