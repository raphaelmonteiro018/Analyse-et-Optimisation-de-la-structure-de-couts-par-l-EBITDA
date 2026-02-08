# 📈 Analyse descriptive & Modélisation

## 🎯 Objectifs
- Poser un cadre analytique rigoureux avant toute simulation de redressement.
- Récupérer et fiabiliser les données issues du P&L consolidé.
- Identifier les moteurs de la perte opérationnelle (EBITDA négatif).
- Vérifier l’existence de leviers d’optimisation par département.
- Éviter toute coupe budgétaire arbitraire avant la phase de modélisation économétrique.

## 🔗 Sources des données
Les données proviennent d'un dataset fictif récupéré pour l'exercice :
- P&L opérationnel : Détail des revenus et charges par business Unit (East, North, South, West).
- Référentiel coûts : Ventilation par poste de dépense (marketing, RH, IT, loyer, admin, force de vente).
- Temporalité des données : Historique journalier pour les ventes et mensuel pour les budgets par région/poste de dépense.

## 🗓️ Harmonisation & Préparation
Afin d’assurer une comparabilité parfaite entre les différentes Business Units :
- Alignement calendaire : Toutes les données sont agrégées sur une base hebdomadaire stable.
- Pivotage des données (ETL) : Transformation du format transactionnel (lignes de coûts) en format analytique (colonnes par département) via un pipeline Python.
- Normalisation des métriques : Calcul systématique du taux de marge brute et de l'EBITDA normalisé pour éliminer les effets de périmètre.

## ⚙️ Ingénierie des données & Variable cible (Y)
- Variable cible (Y) : L'EBITDA hebdomadaire est retenu comme l'indicateur maître de la performance.
- Indicateur de survie (point mort) : Calcul du seuil de rentabilité théorique pour chaque branche afin de mesurer l'écart à la rentabilité.
- Feature engineering : Création de ratios d'efficacité commerciale (CA généré par euro de salaire) pour auditer la productivité de la force de vente.

## 🏗️ Diagnostic de la Structure de Coûts
L'analyse porte sur 6 centres de coûts principaux. L'enjeu est de distinguer les coûts "efficients" (générateurs de croissance) des coûts "toxiques" (destructeurs de marge).
- Coûts fixes critiques : Loyer et administration.
- Coûts variables d'acquisition : Marketing et force de vente.
- Supports opérationnels : IT et ressources humaines.

## 📊 Statistiques descriptives
### Comparaison de l'EBITDA et des charges fixes hebdomadaires

Période étudiée : **Historique consolidé (2024-2025)**

| Métrique | EBITDA moyen | Coût Loyer | Coût Force de Vente |
| --- | --- | --- | --- |
| **Moyenne Groupe** | **-1 487,19 €** | **628,22 €** | **773,64 €** |
| **Écart-type** | 425,12 € | 62,50 € | 34,42 € |
| **Minimum** | -1 637,05 € | 581,97 € | 739,83 € |
| **Médiane** | **-1 488,90 €** | 607,04 € | 767,27 € |
| **Maximum** | -1 333,89 € | 716,85 € | 820,22 € |

<img width="1247" height="823" alt="image" src="https://github.com/user-attachments/assets/ad300750-be5f-485a-ac30-278df9255a3d" />

<img width="1494" height="944" alt="image" src="https://github.com/user-attachments/assets/aeb06ab7-21cd-4a4e-9e81-357360ea72db" />

### 💡 Lecture :
- Insolvabilité structurelle : L'EBITDA moyen est négatif sur 100% des Business Units examinées. La médiane de chaque boîte (ligne centrale dans les boîtes) se situe systématiquement sous le seuil de rentabilité de 0 €.
- Analyse des performances atypiques (outliers) : Les points isolés au-dessus de 0 € (notamment sur East-01 et West-01) prouvent que la rentabilité est atteignable ponctuellement, mais qu'elle est étouffée par la rigidité des charges fixes le reste du temps.
- Poids de l'immobilier : Le loyer moyen représente une charge fixe disproportionnée, avec un pic critique à **716,85 €** sur la branche North-01 (voir graphique de structure des OPEX).
- Inefficience commerciale : La force de vente est le premier poste de dépense global, mais sa corrélation avec la croissance de l'EBITDA semble s'essouffler (rendements décroissants).

## 📐 Interprétation du Point Mort
Le déficit médian par rapport au point mort est de **4 362 €**.

- Ce chiffre confirme que la structure actuelle ne peut pas atteindre l'équilibre simplement par une croissance organique des ventes.
- Une **réduction drastique des charges fixes** est mathématiquement indispensable avant d'envisager tout levier de croissance.

## 🔍 Analyse de corrélation préliminaire

Cette étape permet de valider la pertinence des facteurs retenus avant la régression.

### 📊 Matrice de corrélation (Variables Clés)

| Variables | EBITDA | Sales | Cost_Rent | Cost_Sales | Cost_Mkt |
| --- | --- | --- | --- | --- | --- |
| **EBITDA** | 1 | 0,32 | -0,88 | -0,91 | -0,75 |
| **Sales** | 0,32 | 1 | 0,05 | 0,12 | 0,45 |
| **Cost_Rent** | -0,88 | 0,05 | 1 | 0,10 | 0,08 |
| **Cost_Sales** | -0,91 | 0,12 | 0,10 | 1 | 0,15 |

### 🧠 Enseignements
- Forte corrélation négative : Le loyer et la force de vente sont les deux variables les plus corrélées à la dégradation de l'EBITDA (r < -0.85).
- Faible impact des ventes : La corrélation entre les ventes et l'EBITDA est trop faible (0.32), ce qui suggère que chaque euro de CA supplémentaire est "mangé" par des coûts variables trop élevés.
- Validation du modèle : L'absence de colinéarité excessive entre les départements permet de passer à une régression multiple robuste.

## 


