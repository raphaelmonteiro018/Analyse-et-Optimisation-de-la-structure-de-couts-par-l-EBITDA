## 🏢 Contexte
Ce projet vise à diagnostiquer la viabilité financière d'un réseau de business units en difficulté chronique. L'objectif est de transformer des données comptables brutes en un moteur de décision capable d'identifier les centres de coûts toxiques et de simuler une trajectoire de redressement vers l'équilibre (EBITDA).

## 🎯 Objectifs
- Isoler les leviers de perte : Identifier mathématiquement quels départements (loyer, marketing, RH, etc.) détruisent la rentabilité.
- Réduire le risque de faillite : Simuler une restructuration chirurgicale pour abaisser le point mort financier sans stopper l'activité.
- Stress-test du business model : Utiliser la simulation What-if pour tester si le redressement est possible par les coûts ou s'il nécessite un pivot stratégique vers le volume.
- Industrialiser le reporting : Automatiser le flux de données entre l'extraction P&L, l'analyse Python et la génération de feuilles de route opérationnelles sous Excel.

## 🚀 Résultats
- Diagnostic de survie : Mise en évidence que le plan d'austérité seul (coupes de -25% sur les postes critiques) est insuffisant pour atteindre le point mort, réduisant le déficit de seulement 40%.
- Fiabilité du modèle : 98.2% ($R^2$). La variation de l'EBITDA est expliquée quasi intégralement, garantissant des simulations de redressement mathématiquement robustes.
- Identification des leviers toxiques : Mise en évidence d'un effet de levier inversé sur le loyer et la force de vente (coefficients $> |1.0|$), confirmant une structure de coûts surdimensionnée par rapport au volume actuel.
- Pivot vers la croissance : Démonstration que le salut de l'entreprise repose sur un choc de volume, il manque ~2 400 € de CA hebdomadaire par branche pour absorber les charges fixes restantes.

## 🔁 Workflow
1. ETL & Préparation : Consolidation des flux P&L et transformation des données pour créer un dataset exploitable par branche et par semaine.
2. Diagnostic descriptif : Analyse de la dispersion et calcul de la marge de sécurité par rapport au point mort théorique.
3. Moteur économétrique : Déploiement d'une régression linéaire multiple pour quantifier la toxicité des coûts.
4. Stress-test & Prescription : Simulation d'une structure "lean" et export automatisé des plans d'action correctifs par région.

## 🏗️ Outils utilisés
- Python : Pandas, NumPy, Statsmodels, Seaborn, Matplotlib.
- Excel : Automatisation du reporting et génération des mémos de redressement.

## 📁 Contenu du projet
- Etape 1 : Analyse descriptive & Modélisation
- Etape 2 : Choix des leviers & Simulation du redressement

## Navigation
Pour naviguer entre les différentes étapes du processus, veuillez sélectionner les branches dans l'ordre suivant :
<img width="1852" height="542" alt="image" src="https://github.com/user-attachments/assets/4caed3ab-4151-4916-a118-1ca66b3adceb" />
