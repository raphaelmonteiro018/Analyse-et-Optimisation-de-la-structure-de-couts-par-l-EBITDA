## 🏢 Contexte
Ce projet vise à diagnostiquer la viabilité financière d'un réseau de business units en difficulté chronique. L'objectif est de transformer des données comptables brutes en un moteur de décision capable d'identifier les centres de coûts toxiques et de simuler une trajectoire de redressement vers l'équilibre (EBITDA).

## 🎯 Objectifs
* **Isoler les leviers de perte** : Identifier mathématiquement quels départements (Loyer, Marketing, RH, etc.) détruisent la rentabilité opérationnelle.
* **Réduire le risque de faillite** : Simuler une restructuration chirurgicale pour abaisser le point mort financier sans stopper l'activité.
* **Auditer la structure de coûts** : Proposer une méthodologie économétrique (Régression OLS) permettant de justifier chaque coupe budgétaire par son impact réel sur l'EBITDA.
* **Industrialiser le reporting** : Automatiser le flux de données entre l'extraction P&L, l'analyse Python et la génération de feuilles de route opérationnelles sous Excel/VBA.

## 🚀 Résultats

* **Réduction du Point Mort : -37%** de chiffre d'affaires nécessaire pour atteindre l'équilibre financier grâce à l'optimisation des charges fixes.
* **Fiabilité du Modèle : 98.2% (R-squared)**. La variation de l'EBITDA est expliquée quasi intégralement par les variables de coûts et de revenus identifiées.
* **Optimisation de l'EBITDA** : Amélioration de la performance de **+966 € par semaine et par branche**, ramenant le déficit de -1487 € à -520 € dans un scénario conservateur.
* **Aide à la décision stratégique** : Mise en évidence du "plafond de verre" du business model actuel, prouvant la nécessité d'un pivot produit malgré une gestion optimisée.

## 🔁 Workflow

1. **ETL & Préparation (VBA/Python)** : Consolidation des flux P&L et pivotage des données pour créer un dataset exploitable par branche et par semaine.
2. **Diagnostic Descriptif** : Analyse de la dispersion (Boxplots) et calcul de la marge de sécurité par rapport au point mort théorique.
3. **Moteur Économétrique** : Déploiement d'une régression linéaire multiple pour quantifier la toxicité des coûts (coefficients d'impact).
4. **Stress-Test & Prescription** : Simulation d'une structure "Lean" et export automatisé des plans d'action correctifs par région.

## 🏗️ Outils utilisés

* **Python** : Pandas, NumPy, Statsmodels (Économétrie), Seaborn/Matplotlib.
* **Excel & VBA** : Automatisation du reporting et génération des mémos de redressement.
* **Concepts Financiers** : Analyse marginale, Point Mort (Break-even), EBITDA, OPEX Optimization.

## 📁 Contenu du projet

* **Etape 1 : Analyse descriptive** - Mise en évidence de l'insolvabilité de la structure actuelle.
* **Etape 2 : Modélisation MLR** - Calcul des coefficients d'impact et identification des départements critiques.
* **Etape 3 : Simulation de Redressement** - Projection de l'EBITDA après activation des leviers d'optimisation.

## Navigation

Pour naviguer entre les différentes étapes du processus, veuillez sélectionner les scripts dans l'ordre suivant :

1. `ANALYSE_DESCRIPTIVE.py`
2. `MLR_MODEL.py`
3. `REDRESSEMENT_CIBLE.py`

---

### Un petit conseil pour la suite :

Pense à inclure tes captures d'écran (`image_b54045.png` pour la dispersion et `image_b5a55a.png` pour le stress-test) juste en dessous des sections **Résultats** ou **Workflow**. Ça donnera exactement le même aspect visuel que ton exemple.

**Est-ce que cette structure te convient pour ton profil GitHub ?**
