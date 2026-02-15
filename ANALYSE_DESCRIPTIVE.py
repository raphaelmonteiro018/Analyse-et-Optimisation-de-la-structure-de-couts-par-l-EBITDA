import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# =============================================================================
# 1. CHARGEMENT ET PRÉPARATION DU DATASET
# =============================================================================
# Importation des données financières retraitées (P&L analytique)
try:
    df = pd.read_excel('pnl_ready_for_mlr.xlsx')
except FileNotFoundError:
    print("Erreur : Fichier source 'pnl_ready_for_mlr.xlsx' introuvable.")
    exit()

# =============================================================================
# 2. AUDIT STATISTIQUE DES INDICATEURS CLÉS (KPIs)
# =============================================================================
# Analyse de la distribution des variables critiques : Revenus, Volumes et Rentabilité
cols_analyse = ['Sales', 'Quantity', 'OPEX_Total', 'EBITDA', 'BreakEven_Sales']
stats_extending = df[cols_analyse].describe(percentiles=[.1, .25, .5, .75, .9])

print("--- ANALYSE STATISTIQUE AVANCÉE (MÉMOIRE FINANCIER) ---")
print(stats_extending)

# =============================================================================
# 3. DIAGNOSTIC DE SOLVABILITÉ ET MARGE DE SÉCURITÉ
# =============================================================================
# Calcul de l'écart opérationnel par rapport au seuil de rentabilité théorique
df['Safety_Margin'] = df['Sales'] - df['BreakEven_Sales']
margin_mediane = df['Safety_Margin'].median()
margin_10th = df['Safety_Margin'].quantile(0.1)

print(f"\nDiagnostic de Survie Opérationnelle :")
print(f"  > Déficit de Sales critique (10e percentile) : {margin_10th:.2f} €")
print(f"  > Écart médian au Point Mort                 : {margin_mediane:.2f} €")

# Alerte de viabilité structurelle
if margin_mediane < 0:
    print("  ⚠️ ALERTE STRATÉGIQUE : La performance médiane est inférieure au point mort.")

# =============================================================================
# 4. VISUALISATION A : DISPERSION ET VOLATILITÉ DE L'EBITDA
# =============================================================================
plt.figure(figsize=(10, 7))

# Représentation par boîtes à moustaches pour isoler la variance inter-branches
sns.boxplot(
    x='Branch', 
    y='EBITDA', 
    data=df, 
    palette='OrRd', 
    width=0.6,
    flierprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "gray", "markersize": 5}
)

# Configuration des référentiels et titres
plt.axhline(0, color='black', linestyle='--', linewidth=1.5, label='Seuil de Rentabilité (0 €)')
plt.plot([], [], 'o', markerfacecolor='white', markeredgecolor='gray', label='Outliers (Performances atypiques)')

plt.title('DISPERSION DE L\'EBITDA PAR BUSINESS UNIT', fontsize=14, fontweight='bold', pad=25)
plt.xlabel('Business Unit', fontsize=11, fontweight='bold', labelpad=15)
plt.ylabel('EBITDA HEBDOMADAIRE (en Euros €)', fontsize=11, fontweight='bold', labelpad=15)

# Optimisation de la légende et de la grille pour lecture C-Level
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=True, fontsize=10)
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout(rect=[0, 0.05, 1, 1]) 
plt.savefig('01_Dispersion_EBITDA.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 5. VISUALISATION B : ANALYSE DE LA STRUCTURE DES CHARGES (OPEX)
# =============================================================================
plt.figure(figsize=(12, 8))

# Agrégation des centres de coûts pour l'analyse de la structure de dépenses
cost_cols = [c for c in df.columns if c.startswith('Cost_')]
df_costs = df.groupby('Branch')[cost_cols].mean()

# Visualisation empilée pour identifier le poids relatif de chaque poste d'OPEX
df_costs.plot(kind='bar', stacked=True, colormap='viridis', width=0.7, ax=plt.gca())

plt.title('COMPOSITION MOYENNE DES OPEX PAR BUSINESS UNIT', fontsize=14, fontweight='bold', pad=25)
plt.xlabel('Business Unit', fontsize=11, fontweight='bold', labelpad=15)
plt.ylabel('MONTANT DES CHARGES HEBDOMADAIRES (en Euros €)', fontsize=11, fontweight='bold', labelpad=15)

# Configuration de la légende pour une distinction rapide des départements
plt.legend(title="Postes de Dépenses", loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=True)

plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('02_Structure_Couts.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 6. VALIDATION ET EXPORT
# =============================================================================
print("\n" + "="*50)
print("✅ Pipeline d'Analyse Descriptive finalisé.")
print("📁 Assets graphiques générés :")
print("    1. 01_Dispersion_EBITDA.png")
print("    2. 02_Structure_Couts.png")
print("="*50)