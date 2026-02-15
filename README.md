## 📈 Simulation du plan de redressement

L'objectif est de tester la viabilité d'un plan de retour à l'équilibre en activant les leviers identifiés par la régression OLS.

### 🛠️ Stratégie : Le scénario de "Rigueur Opérationnelle"

Le plan repose sur un arbitrage différencié des ressources pour sortir du déficit chronique (moyenne groupe de **-1 487 € / semaine**) :

**1. Choc opérationnel différencié (Coupes ciblées)**
- 🔴 Postes toxiques **(-25 %)** : Loyer (`Cost_Rent`) et Force de vente (`Cost_Sales`)
- ➖ Postes neutres **(-15 %)** : Marketing et Administration
- ✅ Postes efficients **(-10 %)** : IT — on préserve l'outil de production

**2. Choc de valeur (Sourcing)**
- Objectif : **+0,50 point de marge brute**, soit un gain de **+13,36 € d'EBITDA hebdo** selon le coefficient de sensibilité

---

### 📊 Résultats de la simulation

L'application de ces mesures montre un redressement significatif, mais **insuffisant pour atteindre le point mort** (Break-even).

| Branche | EBITDA Initial | Gain (Coûts + Valeur) | EBITDA Projeté | Statut |
|---|---|---|---|---|
| East-01 | -1 524 € | +557 € | -967 € | 🔴 Déficitaire |
| North-01 | -1 637 € | +606 € | -1 031 € | 🔴 Déficitaire |
| South-01 | -1 334 € | +565 € | -769 € | 🔴 Déficitaire |
| West-01 | -1 454 € | +584 € | -869 € | 🔴 Déficitaire |

---

### 🧠 Diagnostic

Cette simulation est capitale car elle démontre mathématiquement que **l'austérité seule est une impasse** :

**Le mur des coûts fixes** — Même en coupant 25 % des loyers et des salaires commerciaux, le gain moyen (~580 €) ne couvre pas la perte initiale. La structure de coûts est trop rigide par rapport au volume d'affaires actuel.

**L'insuffisance du levier de marge brute** — Bien que le coefficient soit élevé (2 671), une hausse de 0,5 pt de marge est une goutte d'eau (+13 €) face à l'ampleur du déficit hebdomadaire.

**La variable manquante : le Volume (`Sales`)** — Le modèle confirme que sans un choc massif de croissance du Chiffre d'Affaires (coefficient +0,38), la rentabilité est inatteignable.

---

### 🚀 Conclusion & Décision stratégique

Le plan de redressement **V1 (Rigueur) échoue**. Pour sauver les Business Units, la recommandation stratégique doit pivoter vers une **croissance agressive**.

Pour combler les ~900 € manquants, il est impératif de générer environ **2 400 € de ventes supplémentaires par semaine** ($900 / 0,38$).

> **Verdict** : Le redressement ne passera pas par les économies, mais par la **reconquête commerciale** et l'atteinte de la **taille critique**.
