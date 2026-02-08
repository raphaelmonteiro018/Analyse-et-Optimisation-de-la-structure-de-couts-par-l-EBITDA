## 🏢 Contexte
Ce projet vise à diagnostiquer la viabilité financière d'un réseau de business units en difficulté chronique. L'objectif est de transformer des données comptables brutes en un moteur de décision capable d'identifier les centres de coûts toxiques et de simuler une trajectoire de redressement vers l'équilibre (EBITDA).

## 🎯 Objectifs
- Isoler les leviers de perte : Identifier mathématiquement quels départements (loyer, marketing, RH, etc.) détruisent la rentabilité opérationnelle.
- Réduire le risque de faillite : Simuler une restructuration chirurgicale pour abaisser le point mort financier sans stopper l'activité.
- Auditer la structure de coûts : Proposer une méthodologie économétrique (Régression OLS) permettant de justifier chaque coupe budgétaire par son impact réel sur l'EBITDA.
- Industrialiser le reporting : Automatiser le flux de données entre l'extraction P&L, l'analyse Python et la génération de feuilles de route opérationnelles sous Excel.

## 🚀 Résultats
- Réduction du point mort : -37% de chiffre d'affaires nécessaire pour atteindre l'équilibre financier grâce à l'optimisation des charges fixes.
- Fiabilité du modèle : 98.2% (R-squared). La variation de l'EBITDA est expliquée quasiment intégralement par les variables de coûts et de revenus identifiées.
- Optimisation de l'EBITDA : Amélioration de la performance de **+65% en moyenne**, ramenant le déficit de -1487 € à -520 € par semaine et par business unit.
- Aide à la décision stratégique : Mise en évidence du "plafond de verre" du business model actuel, prouvant la nécessité d'un pivot stratégique malgré une gestion optimisée.

## 🔁 Workflow
1. ETL & Préparation : Consolidation des flux P&L et transformation des données pour créer un dataset exploitable par branche et par semaine.
2. Diagnostic descriptif : Analyse de la dispersion et calcul de la marge de sécurité par rapport au point mort théorique.
3. Moteur économétrique : Déploiement d'une régression linéaire multiple pour quantifier la toxicité des coûts.
4. Stress-test & Prescription : Simulation d'une structure "lean" et export automatisé des plans d'action correctifs par région.

## 🏗️ Outils utilisés
- Python : Pandas, NumPy, Statsmodels, Seaborn, Matplotlib.
- Excel : Automatisation du reporting et génération des mémos de redressement.

## 📁 Contenu du projet
- Etape 1 : Analyse descriptive - Mise en évidence de l'insolvabilité de la structure actuelle.
- Etape 2 : Modélisation MLR - Calcul des coefficients d'impact et identification des départements critiques.
- Etape 3 : Simulation de redressement - Projection de l'EBITDA après activation des leviers d'optimisation.

## Navigation
Pour naviguer entre les différentes étapes du processus, veuillez sélectionner les scripts dans l'ordre suivant :
<img width="1852" height="542" alt="image" src="https://github.com/user-attachments/assets/4caed3ab-4151-4916-a118-1ca66b3adceb" />
