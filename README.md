Fatality Predictor - README

Introduction

Ce projet vise à prédire la gravité des accidents de la route à partir de données issues de plusieurs sources. L’objectif est d’identifier les facteurs influençant la gravité des accidents afin d’améliorer la prévention et la sécurité routière.

Les modèles prédictifs sont entraînés pour classifier chaque accident selon trois niveaux de gravité :
• 0 : Accident mineur (sans blessé grave)
• 1 : Accident avec au moins un blessé grave, mais aucun décès
• 2 : Accident mortel (au moins un décès)

Les données proviennent de plusieurs jeux de données distincts, nécessitant une étape préalable de fusion et de transformation pour exploiter toutes les informations de manière cohérente.

Structure du Projet

Le projet est organisé en trois notebooks principaux et huit fichiers de données.

Notebooks

1.	FatalityDetector_Notebook_Part_1.ipynb

• Nettoyage et exploration des données
• Fusion des différents fichiers de données
• Feature engineering pour enrichir les variables explicatives
• Génération du dataset final (X_train et X_test)

2.	FatalityDetector_Notebook_Part_2.ipynb

• Entraînement de plusieurs modèles de machine learning
• Sélection des 5 meilleurs modèles
• Optimisation des hyperparamètres
• Génération des prédictions finales sur X_test

3.	FatalityDetector_Notebook_Part_3.ipynb

• Évaluation finale des modèles sur y_test
• Comparaison des scores d’accuracy

Fichiers de Données

• caracteristiques_clean.csv : Informations sur les conditions et caractéristiques des accidents
• lieux_clean.csv : Données sur l’environnement géographique des accidents
• vehicules_clean.csv : Caractéristiques des véhicules impliqués
• usagers_clean.csv : Informations sur les conducteurs et passagers impliqués
• X_train.csv : Ensemble d’entraînement des modèles
• X_test.csv : Données de test pour évaluer les modèles
• y_test.csv : Vérités terrain pour évaluer les modèles
• y_pred.csv : Prédictions finales des modèles et vote majoritaire
 

Approche et Méthodologie

1.	Prétraitement des Données (Notebook 1)

• Nettoyage des datasets (suppression des valeurs aberrantes et des variables inutiles)
• Fusion des fichiers en un dataset exploitable
• Feature Engineering :
• Extraction d’informations temporelles (jour, saison, moment de la journée)
• Catégorisation des types de routes et véhicules
• Création de nouvelles variables sur les conditions météo et la configuration des accidents
• Encodage et normalisation des données pour la modélisation

2.	Modélisation et Sélection des Meilleurs Modèles (Notebook 2)

• Entraînement de 10 modèles différents, incluant : Régression Logistique, Random Forest, Gradient Boosting, SVM, MLP (Neural Network), etc.
• Pondération des classes pour mieux gérer le déséquilibre des classes
• Sélection des 5 meilleurs modèles sur X_val
• Optimisation des hyperparamètres via GridSearchCV
• Génération des prédictions finales sur X_test
 
Résultats

Meilleures performances obtenues sur X_test :

Modèle	Accuracy
Gradient Boosting	71.26%
HistGradientBoosting	70.90%
Vote majoritaire	70.49%
Random Forest	68.60%
AdaBoost	68.53%
MLP (Neural Network)	68.06%
	
Observations clés :
• Le Gradient Boosting et HistGradientBoosting sont les modèles les plus performants.
• Le vote majoritaire améliore la stabilité en combinant les forces de plusieurs modèles.
• Les accidents mortels (classe 2) restent sous-estimés, malgré la pondération des classes.
• La gestion du déséquilibre de classes reste un défi, et d’autres approches pourraient être explorées (perte personnalisée, rééchantillonnage, etc.).
 
Conclusion

Ce projet a permis de développer un modèle de machine learning prédictif de la gravité des accidents de la route, en exploitant plusieurs sources de données et en optimisant les performances des modèles.
Le Gradient Boosting s’est révélé être le modèle le plus performant, et le vote majoritaire a permis d’améliorer la robustesse des prédictions.
L’approche pourrait être affinée avec des méthodes avancées pour mieux gérer le déséquilibre des classes et affiner les prédictions des accidents mortels. 


Projet réalisé avec Scikit-Learn, Pandas, NumPy, et Seaborn
Auteurs : Sacha Abitbol, Maxime Appert, Selyan Chergui
