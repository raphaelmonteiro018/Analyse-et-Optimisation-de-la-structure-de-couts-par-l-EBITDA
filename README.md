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

## 🏗️ Diagnostic de la structure de coûts
L'analyse porte sur 6 centres de coûts principaux. L'enjeu est de distinguer les coûts "efficients" (générateurs de croissance) des coûts "toxiques" (destructeurs de marge).
- Coûts fixes critiques : Loyer et administration.
- Coûts variables d'acquisition : Marketing et force de vente.
- Supports opérationnels : IT et ressources humaines.

## 📊 Statistiques descriptives
### Comparaison de l'EBITDA et des charges fixes hebdomadaires par business unit

Période étudiée : **Historique consolidé (2024-2025)**

| Métrique | EBITDA moyen | Coût Loyer | Coût Force de Vente |
| --- | --- | --- | --- |
| **Moyenne Groupe** | **-1 487,19 €** | **628,22 €** | **773,64 €** |
| **Écart-type** | 425,12 € | 62,50 € | 34,42 € |
| **Minimum** | -1 637,05 € | 581,97 € | 739,83 € |
| **Médiane** | **-1 488,90 €** | 607,04 € | 767,27 € |
| **Maximum** | -1 333,89 € | 716,85 € | 820,22 € |
------------------------------------------------------------------
<img width="1524" height="834" alt="image" src="https://github.com/user-attachments/assets/66202d06-609a-4349-91af-fbeb3238d80e" />

<img width="1611" height="943" alt="image" src="https://github.com/user-attachments/assets/57e299af-fe22-462b-a674-730d431a0301" />

### 💡 Lecture :
- Insolvabilité structurelle : L'EBITDA moyen est négatif sur 100% des business units examinées. La médiane de chaque boîte (ligne centrale dans les boîtes) se situe systématiquement sous le seuil de rentabilité de 0 €.
- Analyse des performances atypiques (outliers) : Les points isolés au-dessus de 0 € (notamment sur East-01 et West-01) prouvent que la rentabilité est atteignable ponctuellement, mais qu'elle est étouffée par la rigidité des charges fixes le reste du temps.
- Poids de l'immobilier : Le loyer moyen représente une charge fixe disproportionnée, avec un pic critique à **716,85 €** sur la branche North-01 (voir graphique de structure des OPEX).
- Inefficience commerciale : La force de vente est le premier poste de dépense global, mais sa corrélation avec la croissance de l'EBITDA semble s'essouffler (rendements décroissants).

## 📐 Interprétation du point mort
Le déficit médian par rapport au point mort consolidé est de **4 362 €**.

- Ce chiffre confirme que la structure actuelle ne peut pas atteindre l'équilibre simplement par une croissance organique des ventes.
- Une **réduction drastique des charges fixes** est mathématiquement indispensable avant d'envisager tout levier de croissance.

## ⚖️ Modélisation Économétrique

Une analyse de corrélation a été réalisée pour valider la sélection des variables et identifier les moteurs de perte, puis, une régression linéaire multiple par la méthode des moindres carrés ordinaires (OLS) a été déployée afin de quantifier l’impact marginal de chaque poste de dépense sur l’EBITDA.

## 🔍 Analyse des corrélations
<img width="945" height="793" alt="image" src="https://github.com/user-attachments/assets/998619eb-c479-4f14-a884-0ee822f0a793" />
---------------------------------------------------------
- On observe une corrélation positive très forte de 0,8922 entre le volume de ventes et l'EBITDA. Cela confirme que le modèle est sensible au volume, mais que la structure de coûts actuelle "étouffe" ce levier.
- La matrice confirme que certains coûts, bien que nécessaires, ont un impact négatif marqué sur l'EBITDA lorsqu'ils ne sont pas optimisés.
- Les faibles corrélations croisées entre les différents postes de dépenses (souvent proches de 0) permettent d'éviter le biais de multicolinéarité, garantissant la fiabilité des coefficients de la régression OLS.

## 📊 Performance du modèle
- Coefficient de détermination ($R^2$) : 0,982  
  Le modèle explique **98,2 % des variations de l’EBITDA**, garantissant une fiabilité extrême pour les simulations de redressement.
- Significativité globale (Prob F-stat) : $1,44 \times 10^{-321}$  
  La probabilité que les relations observées soient dues au hasard est quasi nulle.
- Indice de confiance : Toutes les variables présentent une **P-value ≈ 0,000**, confirmant leur pertinence statistique individuelle.

## 🔍 Analyse des coefficients ($\beta$)
L’équation de régression permet d’isoler la toxicité ou l’efficience de chaque euro engagé :

| Variable | Coefficient | Nature de l’impact | Diagnostic stratégique |
|--------|-------------|-------------------|------------------------|
| **Gross_Margin_Rate** | **+2 671,72** | Crucial | Levier principal de rentabilité via le prix et le mix produit. |
| **Sales** | +0,3813 | Modéré | Chaque euro de CA ne génère que 0,38 € d’EBITDA net. |
| **Cost_IT** | -0,8970 | Efficient | Investissement utile, coût support nécessaire. |
| **Cost_Admin** | -0,9888 | Neutre | Structure de coût fixe standard. |
| **Cost_Marketing** | -0,9941 | Inefficient | Le marketing détruit plus d’EBITDA qu’il n’en génère directement. |
| **Cost_Sales** | **-1,0406** | Toxique | Sureffectif ou inefficacité structurelle de la force de vente. |
| **Cost_Rent** | **-1,0546** | Toxique | Loyer surévalué par rapport à la capacité de génération de cash. |

### Test de fiabilité des prévisions
<img width="802" height="480" alt="image" src="https://github.com/user-attachments/assets/934318c8-873c-4135-ae12-be95b804e089" />
--------------------------------------------------------------------------

## 🧠 Enseignements Stratégiques
- Priorisation des coupes : Les départements dont le coefficient est supérieur à $|1,0|$ (**Rent** et **Sales Force**) sont les cibles prioritaires.
  Chaque euro économisé dans ces pôles améliore l’EBITDA de **plus d’un euro**, traduisant un fort effet de levier sur les coûts fixes.
- Seuil d’efficience IT : 1vec un coefficient de **-0,90**, l’IT est le département le plus efficient en coût support.  
  Une réduction budgétaire aurait un impact négatif disproportionné sur l’EBITDA.
- Faiblesse du levier CA : Le coefficient des ventes (**0,38**) confirme que la croissance du chiffre d’affaires seule ne permet pas de redresser la structure sans une révision profonde de la base de coûts.

## ➡️ Prochaine étape
👉 **Simulation de redressement ciblé**
- Activation des leviers sur les pôles à forte toxicité.
- Projection de l’EBITDA cible post-optimisation.
- Recalcul du point mort et évaluation de la viabilité long terme.


