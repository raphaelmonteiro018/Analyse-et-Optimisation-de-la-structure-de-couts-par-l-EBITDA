# 📈 Analyse descriptive & Modélisation

## 🎯 Objectifs
- Poser un cadre analytique rigoureux avant toute simulation de redressement.
- Récupérer et fiabiliser les données issues du P&L consolidé.
- Identifier les moteurs de la perte opérationnelle (EBITDA négatif).
- Vérifier l’existence de leviers d’optimisation par département.
- Éviter toute coupe budgétaire arbitraire avant la phase de modélisation.

## 🔗 Sources des données
Les données proviennent d'un dataset fictif récupéré pour l'exercice :
- P&L opérationnel : Détail des revenus et charges par business Unit (East, North, South, West).
- Référentiel coûts : Ventilation par poste de dépense (marketing, RH, IT, loyer, admin, force de vente).
- Temporalité des données : L'historique est journalier pour les ventes, et mensuel pour les budgets.

## 🗓️ Harmonisation & Préparation
- Alignement calendaire : Toutes les données sont agrégées sur une base hebdomadaire stable.
- Calcul des indicateurs de rentabilité clés (taux de marge brute, point mort, EBITDA) sur base hebdomadaire par business unit.

## ⚙️ Ingénierie des données & Variable cible (Y)
- Variable cible (Y) : L'EBITDA hebdomadaire est retenu comme le KPI clef.
- Indicateur de survie (point mort) : Calcul du seuil de rentabilité théorique pour chaque branche afin de mesurer l'écart à la rentabilité.

## 🏗️ Diagnostic de la structure de coûts
L'analyse porte sur 6 centres de coûts. L'enjeu est de distinguer les coûts efficients des coûts toxiques.
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

## ⚖️ Modélisation Économétrique
Une analyse de corrélation a été réalisée pour valider la sélection des variables et identifier les moteurs de perte, puis, une régression linéaire multiple par la méthode des moindres carrés ordinaires (OLS) a été déployée afin de quantifier l’impact marginal de chaque poste de dépense sur l’EBITDA.

## 🔍 Analyse des corrélations
<img width="945" height="793" alt="image" src="https://github.com/user-attachments/assets/998619eb-c479-4f14-a884-0ee822f0a793" />

- On observe une corrélation positive très forte de 0,8922 entre le volume de ventes et l'EBITDA. Cela confirme que le modèle est sensible au volume, mais que la structure de coûts actuelle étouffe ce levier.
- La matrice confirme que certains coûts, bien que nécessaires, ont un impact négatif marqué sur l'EBITDA lorsqu'ils ne sont pas optimisés.
- Les faibles corrélations croisées entre les différents postes de dépenses (souvent proches de 0) permettent d'éviter le biais de multicolinéarité, garantissant la fiabilité des coefficients de la régression OLS.

## 📊 Performance du modèle
- Coefficient de détermination ($R^2$) : 0,982  
  Le modèle explique **98,2 % des variations de l’EBITDA**, garantissant la fiabilité des simulations de redressement.
- Indice de confiance : Toutes les variables présentent des **P-value ≈ 0,000**, confirmant leur pertinence statistique individuelle (significativité).

## 🔍 Analyse des coefficients ($\beta$)
L’équation de régression permet d’isoler la toxicité ou l’efficience de chaque euro engagé :

| Variable | Coefficient (β) | Impact Monétaire Réel | Diagnostic stratégique |
|---|---|---|---|
| Gross_Margin_Rate | +2 671,72 | +1 pt de marge = +26,72 € d'EBITDA | ⚙️ **Levier de précision** : Crucial pour la santé à long terme, mais impact faible avec les volumes actuels. |
| Sales | +0,3813 | +1000 € de CA = +381,30 € d'EBITDA | 🚀 **Moteur de cash-flow** : Le levier le plus puissant pour couvrir les charges fixes. |
| Cost_IT | -0,8970 | 100 € coupés sur ce poste = +89,70 € d'EBITDA | ✅ **Efficient** : Coût support nécessaire, couper ici dégrade l'opérationnel. |
| Cost_Admin | -0,9888 | 100 € coupés sur ce poste = +98,88 € d'EBITDA | ➖ **Neutre** : Structure de coût fixe standard. |
| Cost_Marketing | -0,9941 | 100 € coupés sur ce poste = +99,41 € d'EBITDA | ⚠️ **Inefficient** : Le marketing ne s'autofinance pas dans la structure actuelle, cet investissement censé booster les ventes n'est que très peu rentable. |
| Cost_Sales | -1,0406 | 100 € coupés sur ce poste = +104,06 € d'EBITDA | 🔴 **Toxique** : Inefficience de la force de vente (levier inversé). |
| Cost_Rent | -1,0546 | 100 € coupés sur ce poste = +105,46 € d'EBITDA | 🔴 **Toxique** : Loyer surévalué par rapport à la capacité de génération de cash. |

## 💡 Interprétation des leviers de performance
- Sensibilité au Taux de Marge : Le coefficient de +2 671,72 indique une sensibilité extrême du modèle au pricing. Cependant, l'impact monétaire reste chirurgical, une amélioration de 1 point de pourcentage de la marge ne génère actuellement que **26,72 € d'EBITDA hebdomadaire** supplémentaire. Ce levier est nécessaire mais insuffisant pour combler seul un déficit de 1 500 €.
- Priorisation des coupes budgétaires : Les départements dont le coefficient est supérieur à |1,0| (Rent et Sales Force) sont les cibles prioritaires du plan de redressement. Chaque euro économisé dans ces pôles améliore l'EBITDA de plus d'un euro, ce qui traduit mathématiquement l'élimination d'inefficiences structurelles, comme une surcapacité immobilière ou une sous-productivité commerciale.
- Seuil d'efficience IT : Avec un coefficient de -0,90, l'IT est le département le plus "rentable" en termes de support. Une réduction budgétaire aurait un impact négatif disproportionné sur la capacité opérationnelle pour un gain financier marginal.
- Puissance du levier CA : Le coefficient des ventes (0,38) est le moteur de redressement le plus massif. Générer **5 000 € de chiffre d'affaires supplémentaire** rapporte **1 905 € d'EBITDA**, soit bien plus que n'importe quelle coupe budgétaire réaliste.

### 🛡️ Validation de la robustesse du modèle
<img width="802" height="480" alt="image" src="https://github.com/user-attachments/assets/934318c8-873c-4135-ae12-be95b804e089" />

- La distribution des résidus suit une loi normale centrée sur zéro, confirmant la neutralité statistique du modèle et la fiabilité des coefficients utilisés pour le pilotage du plan de redressement.

## 💡 Déploiement de la stratégie de redressement

### 1️⃣ Levier de précision : Restauration de la marge

Le coefficient de +2 671,72 associé au `Gross_Margin_Rate` confirme que la rentabilité se joue sur le **pricing et les coûts d'achat**. Néanmoins, avec un gain de seulement 26,72 € d'EBITDA hebdomadaire pour 1 point de marge supplémentaire, ce levier doit être couplé à une stratégie de volume actuellement inexistante.

Les axes retenus sont :
- 🔄 **Renégociation agressive des coûts d'achat** (Sourcing)
- 🎯 **Optimisation du mix produit** pour favoriser les références à forte contribution

---

### 2️⃣ Assainissement de la structure (Levier > 1.0)

Les postes **Loyer** (`Cost_Rent`) et **Force de vente** (`Cost_Sales`) sont classés comme 🔴 toxiques. Cela signifie que la structure est actuellement **surdimensionnée** pour le volume d'activité traité.

> ⚠️ **Effet de levier inversé** : Chaque euro économisé sur ces postes augmente l'EBITDA de plus d'un euro. Le plan de redressement devra impérativement passer par une **réduction de la voilure immobilière** et une **restructuration commerciale**.

---

### 3️⃣ Levier de puissance : La croissance de volume

Le diagnostic est sans appel : l'entreprise souffre d'un **manque de taille critique**. Le coefficient `Sales` de 0,38 démontre que le modèle opérationnel est **sain mais étouffé** par les charges fixes.

Pour atteindre le point mort, la priorité absolue est d'augmenter le **volume d'affaires** afin d'amortir les coûts fixes restants. Injecter de la croissance après avoir assaini la base de coûts est la **seule voie vers un EBITDA positif durable**.

## ➡️ Prochaine étape : simulation du plan de redressement
