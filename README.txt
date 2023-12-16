Vous devez développer une application au dessus de votre BDD dénormalisée. Vous utiliserez le langage de votre
choix. Le code source doit être clair et commenté. Différentes parties doivent être clairement identifiées :
— La connexion à MongoDB ;
— Importation de votre dataset respectant le schéma de dénormalisation ;
— Mesures de performances ;
— Les vues.

4.1 Importation des données
Afin de dénormaliser votre dataset en respectant le schéma produit dans le 2ème livrable. Pour ce faire, plusieurs
stratégies sont possibles :
— Développer un script de lecture des CSV pour produire les documents JSON adaptés ;
— Intégrer chaque CSV dans MongoDB puis de faire la conversion avec des requêtes MongoDB (opérateur $lookup,
utilisable en local, pas en sharding) ;
— Utiliser l’outil Studio3t en version professionnelle (demander une licence en amont) ;
— Trouver un logiciel de transformation...

4.2 Mesure de performances
Afin d’évaluation l’efficacité de votre solution, vous devrez développement un programme de test pour chaque
requête de votre cas d’usage. Celui-ci devra pouvoir fournir :
— Execution de chaque requête ;
— Mesurer le temps d’exécution de chaque. Pour cela, la requête doit être exécutée sur l’ensemble de la BDD, au
moins 10 fois (retirer le max et le min), et faire la moyenne. Le temps de récupération des données n’est pas
comptabilisé.
— Mesurer le temps sur différentes configuration de sharding : de 1 à 6 shards(minimum) afin de mesurer l’impact
de la distribution
— Le rapport doit pouvoir mettre en valeur les performances liées à chaque requête, et expliquer les variations
obtenues (explication , observation).
Noté sur 10 points.

4.3 Vues
Vous devrez définir des vues en fonction des requêtes définies précédemment.
4.3.1 Utilisateur standard
Fournir à un utilisateur standard un accès aux résultats des 4 requêtes simples. La vue n’a pas forcément besoin
de fournir la requête mais seulement l’interaction avec elles et une vision sur les données interrogées (ou visulation
si possible).
4.3.2 Analyste/Décisionnaire
Fournir à votre Data Analyst ou votre Business User une vue permettant de fournir les requêtes complexes
proposées. L’interface devra permettre de paramétrer les requêtes avec des valeurs (soit à la main, soit par menu
déroulant).
Une DataViz est fortement recommandée pour les résultats obtenus.
4.3.3 Administrateur
L’administrateur de la base MongoDB doit pouvoir récupérer différentes statistiques pour pouvoir faire évoluer
le cluster en fonction de la charge. La vue doit pouvoir fournir les informations suivantes :
— Les statistiques de distribution des données ;
— Consulter l’état du cluster : nombre de shards, nombre de réplicats par shard ;
— Répartition des données sur les shards (nombre de documents) ;
— Indexes existants sur les données.

4.4 Rendu
Un rapport donnant les mesures de performances de vos requêtes, une description de l’architecture de votre
application et serveurs (MongoDB), une description globale de l’organisation de votre code. Egalement un zip ou Git
pour consulter votre code.
BLe rapport doit être rendu à J+56, soit 8 semaines après réception du sujet. Une pénalité de 1 point par jour
de retard sera appliqué.
Noté sur 10 points.
