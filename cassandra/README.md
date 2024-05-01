# TP Cassandra - ESGI 3 IABD

Ce TP vous servira d'introduction à la base de donnée orientée colonne en utilisant un DMBS Cassandra.
Ceci fait l'objet d'un TP noté, vous avez jusqu'à la ~~prochaine alternance~~ trois semaines à partir de la mise à jour 
du présent sujet pour le finaliser.

Le sujet est maintenant dans sa phase quasi-définitif, n'hésitez pas à faire des retours pour le perfectionner.

Rendu attendu sur MyGES :
-  Rapport d'activité du TP, retraçant l'ensemble de vos travaux
   - Pour information : Le rapport contiendra essentiellement les captures d'écrans des résultats d'executions de vos 
   requêtes. 
-  Scripts CQL

Grille de notation ; 
- 1 point par question.
- La réponse aux questions se réalise à travers les captures d'écran de résultats de la commande associé.
- La note finale est ramené sur 20.

## 0. Mise en place de l'architecture

Ouvrez un terminal et tapez la commande suivante : `docker compose up`
Cela devra télécharger une image cassandra, puis le lancer automatiquement.

Vous avez maintenant le choix de continuer le TP sur l'un des deux parcours :
- Le parcours interactif à l'aide de DataGrip
- Le parcours en terminal

> Tips : Datagrip est un outil permettant de requêter sur différents types de DBMS. Elle est incluses dans votre licence
> éducation de JetBrains.
> Référez-vous au slides de Java pour la démarche à réaliser pour la demande de licence étudiante.

## 1. Etat du cluster

Puisque nous avons utilisé `docker compose` pour vous affranchir de la partie installation en dur sur vos postes, nous 
allons devoir exécuter certaines commandes de la maintenance directement depuis le terminal du container docker.

Deux choix s'offrent à vous :
* Le terminal depuis Docker Desktop (Non recommandé car, il y a un manque d'ergonomie)
* Via votre propre terminale
* (Attendu : Capture d'écran + explication des commandes)
---

### Option 1 : Depuis Docker Desktop

* Pour cela, vous allez tout d'abord ouvrir Docker Desktop
* Ensuite, allez dans Containers.
* Puis, cherchez le container cassandra-1 et cliquez dessus (littéralement sur le nom).

> Vous devriez normalement voir le container sur le volet de gauche et les logs sur le volet droit.

* Cliquez sur le container sur le volet de gauche
> Vous devriez voir plusieurs onglets tel que Logs, Inspect, Bind mounts, Exec, Files et Stat.

* Cliquez sur Exec

> Nous y sommes ! Nous avons ouvert un terminal depuis Docker Destop pour vers le container de Cassandra. C'est comme si
> nous avions une machine virtuelle à notre disposition. Nous pouvons maintenant continuer à tapper des commandes de 
> maintenances.

### Option 2 : Depuis votre terminal
* Pour cela, lancez le terminal de votre choix
* Saisissez la commande suivante : `docker exec -it cassandra-1 bash`
---

* Tapez la commande et décrivez leur action réalisée :

```bash
nodetool info
nodetool status
```

> Vous pouvez accéder à la liste des commandes disponibles de nodetool en ayant l'argument `help`

---

## 2. Création d'un keyspace

Un keyspace est un espace où l'on crée des tables. 
Vous allez chacun(e) créer le vôtre, admettons que nous créons une keyspace de nom esgi_cassandra

```cassandraql
CREATE KEYSPACE IF NOT EXISTS esgi_cassandra
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor':2};
```

> Note : La version du docker-compose.yml a été modifié. Il manquait un deuxème node pour Cassandra afin que la 
> réplication des données à 2 fonctionne.

* (Attendu : Capture d'écran)
---
Nous créons ainsi une base de données `esgi_cassandra` pour laquelle le facteur de réplication est mis à 2. Ce qui 
signifie que nous créons un cluster de deux bases de données contenant des données identiques.

Pour être précis : Supposons que nous avons 5 machines.
Les données vont être répliquées 2 fois seulement, car nous n’avons que 5 machines. Sur un cluster professionnel, 
la réplication pourrait être portée à 3 et avec une stratégie adaptée à sa topologie. La réplication est indépendante de
HDFS, car Cassandra n’est pas sur HDFS, il/elle a ses partitions de disques durs spécifiques

* La stratégie `SimpleStrategy` convient pour les clusters locaux. 
* Pour supprimer un keyspace et son contenu : 

```cassandraql
DROP KEYSPACE esgi_cassandra;
```
* (Attendu : Capture d'écran)
---
* Sous `csqlsh`, vous pouvez maintenant sélectionner la base de données pour vos prochaines requêtes.
> Note : N'oubliez pas de recréer la `KEYSPACE` si vous avez exécuté la commande DROP !
```cassandraql
USE esgi_cassandra;
```
> Tips : Vous pouvez préfixer toutes les tables par nomkeyspace.nomtable 

* Et vous pouvez même afficher la liste des `keyspaces`  existants :

```cassandraql
DESCRIBE KEYSPACES; 
```

* Nous pouvons aller plus loin pour afficher la structure d'un keyspace : Cela va donc afficher toutes les commandes 
servant à le reconstruire ainsi que ses tables.

```cassandraql
DESCRIBE KEYSPACE nomkeyspace;
```
* Pour obtenir des informations concernant le cluster, vous pouvez utiliser la commande :
```cassandraql
DESC CLUSTER;
```

* (Attendu : Capture d'écran pour l'ensemble des commandes vu)

## 3. Création d'une table

* Nous allons maintenant créer une table. Elle va donc suivre la logique suivante :

```cassandraql
CREATE TABLE [IF NOT EXISTS] nomdetable(def col);
```

On peut préfixer le nom de la table par `nomkeyspace`.
Les définitions de colonnes sont comme en SQL : `nom type`.

Les types sont `boolean`, `int`, `float`, `varchar`, `text`, `blob`, `timestamp`, etc. Il y a des types spéciaux, comme 
`counter`, `list`, `set`, `map`, etc.

Nous allons utiliser le Dataset suivant pour réaliser la prise en main de Cassandra (normalement fourni avec Github): 
[Lien vers le dataset](https://www.kaggle.com/datasets/muhammadkashif724/netflix-tv-shows-2021)

* Analysez le Dataset de netflix :
    * Récupérez l'ensemble des colonnes de netflix
    * Déterminez les types adéquats
    * Créez les tables

Nous allons donc commencer par créer une table générée par le script qui se situe dans le dossier script et nous allons 
insérer les données csv :

Pour cela, les préparatifs sont déjà réalisé pour vous.

* Connectez vous en bash sur le premier container :
```bash
docker exec -it cassandra1 bash
```
* Naviguez vers le dossier `/script`
* Modifiez le fichier pour choisir un ensemble de clée primaire : nous allons utiliser `title, released_year`

```bash
#!/bin/bash
# définition de la clé primaire
PRIMARY_KEY='(title, release_year)' # Vous devez modifier cette ligne pour que cela fonctionne !
# création de la table
echo "création de la table"
cqlsh -k esgi_cassandra  <<data
CREATE TABLE netflix_shows (
    title TEXT,
    cast SET<TEXT>,
    country TEXT,
    date_added TIMESTAMP,
    release_year INT,
    rating TEXT,
    duration TEXT,
    listed_in SET<TEXT>,
    description TEXT,
    PRIMARY KEY $PRIMARY_KEY
);

data
# pause avant le remplissage (précaution)
sleep 2
# remplissage de la table
echo "remplissage de la table"
cqlsh -k esgi_cassandra master <<data
COPY netflix_shows (...) FROM 'netflix_shows.csv' ...
data
# fin du script
```

* (Attendu : Capture d'écran)

> NB : la notation `<<data...data` est une redirection du script lui-même vers la commande, et elle permet de remplacer 
> les variables bash, comme $LOGNAME et $PRIMARY_KEY. > La ligne vide à la fin est nécessaire avec certains éditeurs de 
> texte.

## 4. Ajout de n-uplets

Nous allons ajouter des données, pour cela, trouvez un moyen d'insérer les données suivantes

Voici les données à insérer :

```
Yu-Gi-Oh! Arc-V,"Mike Liscio, Emily Bauer, Billy Bob Thompson, Alyson Leigh Rosenfeld, Michael Crouch","Japan, Canada",1-May-18,2015,TV-Y7,2 Seasons,"Anime Series, Kids' TV","Now that he's discovered the Pendulum Summoning technique, Yuya's dream of becoming the greatest ""dueltainer"" is in reach – but it won't be easy!"
Yunus Emre,"Gökhan Atalay, Payidar Tüfekçioglu, Baran Akbulut, Mehmet Çepiç, Seda Tosun, Mehmet Ali Tuncer, Asuman Çakır, Müge Uyar, Rüzgar Aksoy, Ergun Taş, Sedat Erdiş, Ahmet Talay, Umut Tanyolu, Murat Ercanlı, Birand Tunca, Atilla Kiliç, Saygin Asan, Emrah Girgin",Turkey,17-Jan-17,2016,TV-PG,2 Seasons,"International TV Shows, TV Dramas","During the Mongol invasions, Yunus Emre leaves his home to travel across the Ottoman Empire, defying hardships and temptations to become a dervish."
Zak Storm,"Michael Johnston, Jessica Gee-George, Christine Marie Cabanos, Christopher Smith, Max Mittelman, Reba Buhr, Kyle Hebert","United States, France, South Korea, Indonesia",13-Sep-18,2016,TV-Y7,3 Seasons,Kids' TV,"Teen surfer Zak Storm is mysteriously transported to the Bermuda Triangle, where he becomes the captain of a magical ship full of misfits."
Zindagi Gulzar Hai,"Sanam Saeed, Fawad Khan, Ayesha Omer, Mehreen Raheel, Sheheryar Munawar, Samina Peerzada, Waseem Abbas, Javed Sheikh, Hina Khawaja Bayat",Pakistan,15-Dec-16,2012,TV-PG,1 Season,"International TV Shows, Romantic TV Shows, TV Dramas","Strong-willed, middle-class Kashaf and carefree, wealthy Zaroon meet in college, but before love can take root, they each have some growing up to do."
```

Si vous vous débrouillez bien, vous n’aurez pas à retaper ces données, seulement à les placer dans un fichier CSV pour 
les charger vers Cassandra.

Nous y reviendrons plus tard pour la manipulation des données de Netflix.

* (Attendu : Capture d'écran)

## 5. Phases de requêtes

Les requêtes sous Cassandra ressemblent très fortement aux requêtes SQL que vous connaissez. Vous allez souvent utiliser 
les clauses telles que `SELECT`, `FROM`, `WHERE`, `ORDER BY`. Vous allez aussi voir que les requêtes sont assez 
restrictifs sur les possibilités.

* Une requête CQL peut seulement retourner des données depuis une table. Ce qui implique la non-présence des jointures 
de tous types.
* Seule les colonnes qui sont déclarées dans la table en tant que clée primaire `PRIMARY KEY` peuvent être utilisé pour 
filtrer, grouper ou bien trier les lignes. L'ordre de définition de la clé primaire doit être respecté lors du filtrage 
et du regroupement, de sorte qu'une clé de partition complète doit être utilisée et que lorsqu'une colonne de clé de 
regroupement est utilisée, toute colonne de regroupement précédente dans la définition de la clé primaire doit également 
être utilisée. 
* Lors de l'ordonnancement des lignes, l'ordre de regroupement déclaré dans la définition de la table doit être 
respecté. L'ordre ne s'applique qu'aux lignes d'une partition et peut-être conservé ou inversé.


Voici la syntaxe des requêtes de CQL

```cassandraql
SELECT [DISTINCT] * | 
       select_expression [AS column_name][ , ... ]
FROM   [keyspace_name.] table_name 
[WHERE partition_key_predicate
  [AND clustering_key_predicate]] 
[GROUP BY primary_key_column_name][ , ... ]
[ORDER BY clustering_key_column_name ASC|DESC][ , ... ]
[PER PARTITION LIMIT number]
[LIMIT number];
```

* La base fondamentale est `SELECT` + `FROM`, qui nous permettra de sélectionner des colonnes depuis une table.
* La clause `WHERE` nous permet de définir une condition.
* La clause `GROUP BY` nous permet de regrouper les données à l'aide d'une colonne ayant la propriété de clée primaire.
* La clause ORDER BY nous permet de trier nos données selon l'attribut ASC ou DESC
* La clause `PER PARTITION LIMIT` nous permet de fixer une limite de ligne dans chaque partition
* La clause `LIMIT` nous permet de limiter le nombre de lignes à afficher


Depuis le terminal docker, nous allons commencer à taper nos premières requêtes en terminal

* Lancez un cassandra interactive, nous aurons besoin d'une keyspace `ks_query`

```
cqlsh -k ks_queries
```
> Remarque : Il faudra créer cette Keyspace avant de pouvoir l'utiliser
> Remarque 2 : N'oubliez pas de saisir la commande `USE`

* Importez la requête suivante
```cassandraql
CREATE TABLE IF NOT EXISTS users (
  email TEXT,
  name TEXT,
  age INT,
  date_joined DATE,
  PRIMARY KEY ((email))
);
INSERT INTO users (email, name, age, date_joined) 
VALUES ('joe@esgi.fr', 'Joe', 25, '2020-01-01');
INSERT INTO users (email, name, age, date_joined) 
VALUES ('jen@esgi.fr', 'Jen', 27, '2020-01-01');
INSERT INTO users (email, name, age, date_joined) 
VALUES ('jim@esgi.fr', 'Jim', 31, '2020-05-07');

CREATE TABLE IF NOT EXISTS movies (
  title TEXT,
  year INT,
  duration INT,
  avg_rating FLOAT,
  PRIMARY KEY ((title, year))
);
INSERT INTO movies (title, year, duration, avg_rating) 
VALUES ('Alice in Wonderland', 2010, 108, 8.33);
INSERT INTO movies (title, year, duration, avg_rating) 
VALUES ('Alice in Wonderland', 1951, 75, 6.5);
INSERT INTO movies (title, year, duration, avg_rating) 
VALUES ('Edward Scissorhands', 1990, 98, 8.5);

CREATE TABLE IF NOT EXISTS ratings_by_user (
  email TEXT,
  title TEXT,
  year INT,
  rating INT,
  PRIMARY KEY ((email), title, year)
) WITH CLUSTERING ORDER BY (title ASC, year DESC);
INSERT INTO ratings_by_user (email, title, year, rating) 
VALUES ('joe@esgi.fr', 'Alice in Wonderland', 2010, 9);
INSERT INTO ratings_by_user (email, title, year, rating)  
VALUES ('joe@esgi.fr', 'Edward Scissorhands', 1990, 10);
INSERT INTO ratings_by_user (email, title, year, rating) 
VALUES ('jen@esgi.fr', 'Alice in Wonderland', 2010, 10);
INSERT INTO ratings_by_user (email, title, year, rating)  
VALUES ('jen@esgi.fr', 'Alice in Wonderland', 1951, 8);
INSERT INTO ratings_by_user (email, title, year, rating) 
VALUES ('jim@esgi.fr', 'Alice in Wonderland', 2010, 6);
INSERT INTO ratings_by_user (email, title, year, rating)  
VALUES ('jim@esgi.fr', 'Edward Scissorhands', 1990, 7);
INSERT INTO ratings_by_user (email, title, year, rating)  
VALUES ('jim@esgi.fr', 'Alice in Wonderland', 1951, 5);

CREATE TABLE IF NOT EXISTS ratings_by_movie (
  title TEXT,
  year INT,
  email TEXT,
  rating INT,
  PRIMARY KEY ((title, year), email)
);
INSERT INTO ratings_by_movie (email, title, year, rating) 
VALUES ('joe@esgi.fr', 'Alice in Wonderland', 2010, 9);
INSERT INTO ratings_by_movie (email, title, year, rating)  
VALUES ('joe@esgi.fr', 'Edward Scissorhands', 1990, 10);
INSERT INTO ratings_by_movie (email, title, year, rating) 
VALUES ('jen@esgi.fr', 'Alice in Wonderland', 2010, 10);
INSERT INTO ratings_by_movie (email, title, year, rating)  
VALUES ('jen@esgi.fr', 'Alice in Wonderland', 1951, 8);
INSERT INTO ratings_by_movie (email, title, year, rating) 
VALUES ('jim@esgi.fr', 'Alice in Wonderland', 2010, 6);
INSERT INTO ratings_by_movie (email, title, year, rating)  
VALUES ('jim@esgi.fr', 'Edward Scissorhands', 1990, 7);
INSERT INTO ratings_by_movie (email, title, year, rating)  
VALUES ('jim@esgi.fr', 'Alice in Wonderland', 1951, 5);
```

* (Attendu : Capture d'écran)

---

### Partie 1 : Users et partitions

* Récupérez les ensembles des lignes contenues dans la table `users`.
* Récupérez une ligne / partition : (Indication, nous allons récupérer les lignes qui ont comme email `joe@esgi.fr`).
* Récupérez deux partitions : (Indication, nous allons récupérer les lignes qui ont comme email `joe@esgi.fr` et 
`jen@esgi.fr`, en utilisant `WHERE` et `IN`)

* (Attendu : Capture d'écran)

---

### Partie 2 Movies et partitions


Nous allons nous intéresser sur les lignes de `movies` :
* Récupérez les ensembles des lignes contenues dans la table `movies`.
* Récupérez une ligne / partition
* Récupérez les deux partitions

* (Attendu : Capture d'écran)

---

Il est totalement possible de créer un script CQL afin de ne pas retaper l'ensemble des commandes à la main.
Pour cela dès maintenant :

Créez un nouveau fichier appelé `requetes.cql` et saisissez l'ensemble des requêtes à partir de la Partie 3.
Pour mettre en commentaire la ligne, vous pouvez utiliser `--` devant la ligne concernée.

Pour charger directement un fichier CQL dans votre base de donnée, vous pouvez saisir la commande suivante (en supposant
que vous l'ayez stocké dans le dossier scripts)

```bash
cqlsh -k nom_keystore < requetes.cql
```

* (Attendu : Capture d'écran)

---

### Partie 3 : Paire de clé primaire pour user et ratings

La table `ratings_by_user` stocke des informations sur les évaluations de films organisées par utilisateurs, de sorte 
que chaque partition contienne toutes les évaluations laissées par un utilisateur particulier. 

Cette table comporte des partitions à plusieurs lignes et la clé primaire est définie comme 
`PRIMARY KEY ((email), title, year)`. Récupérons d'abord toutes les lignes de la table pour savoir à quoi ressemblent 
les données, puis concentrons-nous sur les prédicats que la clé primaire peut prendre en charge.

* Q1. Récupérez toutes les lignes :
* Q2. Récupérez une partition
* Q3. Récupérez deux partitions
* Q4. Récupérez une ligne
* Q5. Récupérez un sous-ensemble de lignes d'une partition (4 exemples attendus)


* (Attendu : Capture d'écran)

---

### Partie 4 : Paire de clé primaire pour movies et ratings

La table `ratings_by_movie` stocke des informations sur les évaluations organisées par film, de sorte que chaque 
partition contienne toutes les évaluations d'un film particulier. 

Cette table comporte des partitions à plusieurs lignes et la clé primaire est définie comme 
`PRIMARY KEY ((title, year), email)`. 

Sans guidage : 
* Récupérons d'abord toutes les lignes de la table pour apprendre à quoi ressemblent les données.
* Concentrons-nous sur les prédicats que la clé primaire peut prendre en charge.
* Pour cela, inspirez-vous de la Partie 3.

* (Attendu : Capture d'écran)

---

### Partie 5 : Aggrégations

Les agrégats CQL comprennent `COUNT`, `SUM`, `AVG`, `MIN` et `MAX`. 
* CQL prend également en charge de nombreuses fonctions, parmi lesquelles nous présenterons `CAST`, `NOW` et `TODATE`. 
Il est possible de créer des agrégats et des fonctions définis par l'utilisateur à l'aide des instructions 
`CREATE AGGREGATE` et `CREATE FUNCTION`. 
* Nous allons créer une fonction pour calculer le nombre de jours entre deux dates. 
* Étudiez et exécutez les exemples de requête suivants.


* Q1. Analysez les scores des filmes

```cassandraql
SELECT COUNT(rating) AS count,
       SUM(rating) AS sum,
       AVG(CAST(rating AS FLOAT)) AS avg,
       MIN(rating) AS min,
       MAX(rating) AS max
FROM   ratings_by_movie
WHERE  title = 'Alice in Wonderland'
  AND  year  = 2010;
```
* Q2. Trouvez le nom de l'utilisateur, la date d'adhésion, et la date actuelle
```cassandraql
SELECT name, 
       date_joined, 
       TODATE(NOW()) AS date_today
FROM   users
WHERE  email = 'joe@esgi.com';
```

* Q3. Calculez le nombre de jours passé depuis l'adhésion

```cassandraql
CREATE FUNCTION IF NOT EXISTS 
  DAYS_BETWEEN_DATES(date1 TEXT, date2 TEXT) 
RETURNS NULL ON NULL INPUT 
RETURNS BIGINT 
LANGUAGE Java AS 
'return java.lang.Math.abs(
   java.time.temporal.ChronoUnit.DAYS.between(
     java.time.LocalDate.parse(date1), 
     java.time.LocalDate.parse(date2)
   )
 );';

SELECT name, 
       DAYS_BETWEEN_DATES( 
         CAST(date_joined   AS TEXT), 
         CAST(TODATE(NOW()) AS TEXT) ) AS days
FROM   users
WHERE  email = 'joe@esgi.com';
```

* (Attendu : Capture d'écran)

---

### Partie 6 : Group

Certaines requêtes peuvent avoir besoin d'organiser les lignes en groupes et de calculer des agrégats pour chaque groupe
individuel. 

Dans Cassandra, le regroupement est toujours basé sur les colonnes de clés de partition et de clustering et doit suivre 
l'ordre de définition de la clé primaire. 

En d'autres termes, un groupe est toujours défini comme un ensemble de lignes appartenant à la même partition. 

* Considérons les exemples de requêtes suivants : 

* Q1. Calculez le score moyen pour tous les films :

```cassandraql
SELECT   title, year,
         AVG(CAST(rating AS FLOAT)) AS avg_rating
FROM     ratings_by_movie
GROUP BY title, year;
```

* Q2. Calculez le score moyen par utilisateur (à trouver)

```cassandraql
SELECT   email, COUNT(rating) AS n
FROM     ratings_by_user
GROUP BY email;
```

* (Attendu : Capture d'écran)


### Partie 7 : Tri des lignes

Cassandra ne trie pas les lignes lors de l'exécution des requêtes. Au lieu de cela, une requête préserve l'ordre de 
regroupement ou l'inverse lors de la récupération des lignes d'une table. Même si ORDER BY n'est pas utilisé, le 
résultat d'une requête conserve l'ordre de regroupement. N'oubliez pas non plus que l'ordre de regroupement s'applique 
aux lignes d'une même partition et ne s'applique pas aux lignes appartenant à des partitions différentes.

Pour la table `ratings_by_user` avec `CLUSTERING ORDER BY (title ASC, year DESC)`, il n'y a que deux options de 
classement, comme indiqué ci-dessous.

* Q1. Utilisez un tri par croissant sur le titre et décroissant sur l'année, depuis `ratings_by_users`
```cassandraql
SELECT * FROM ratings_by_user
WHERE email = 'jim@esgi.com'
ORDER BY title ASC, year DESC;

-- ORDER BY can be omitted 
SELECT * FROM ratings_by_user
WHERE email = 'jim@esgi.com';
```

* Q2. Inversez l'ordre par rapport à la question du dessus :
```cassandraql
SELECT * FROM ratings_by_user
WHERE email = 'jim@esgi.com'
ORDER BY title DESC, year ASC;
```

* (Attendu : Capture d'écran)

### Partie 8 : Limit

Enfin, une requête peut limiter le nombre de lignes renvoyées. Cela est possible grâce aux clauses `PER PARTITION LIMIT` 
et `LIMIT`, qui peuvent être utilisées seules ou ensemble dans la même requête.

Affichez les résultats des requêtes suivantes :

* Q1. En n'utilisant pas les limites :
```cassandraql
SELECT * FROM ratings_by_user
WHERE email IN ('joe@esgi.com',
                'jim@esgi.com');
```

* Q2. En utilisant les limites par partitions :
```cassandraql
SELECT * FROM ratings_by_user
WHERE email IN ('joe@esgi.com',
                'jim@esgi.com')
PER PARTITION LIMIT 2;
```

* Q3. En utilisant globalement la limite :
```cassandraql
SELECT * FROM ratings_by_user
WHERE email IN ('joe@esgi.com',
                'jim@esgi.com')
LIMIT 3;
```

* Q4. En utilisant deux limites à la fois
```cassandraql
SELECT * FROM ratings_by_user
WHERE email IN ('joe@esgi.com',
                'jim@esgi.com')
PER PARTITION LIMIT 2
LIMIT 3;
```

* (Attendu : Capture d'écran + CQL depuis la partie 3)


## 5. De retour sur Netflix

Souvenez-vous que nous avons importé un fichier `csv : netflix_show.csv` à l'aide d'un script bash et que vous avez dû 
trouver une solution pour insérer quatre lignes supplémentaires dans la base de donnée.

Nous allons donc pouvoir mettre en pratique l'ensemble des connaissances acquises dans ce cas pratique !

Dans un fichier cql nommé `netflix_queries.cql` :
* Affichez seulement les titres et années des séries.
* Affichez les séries qui sont sorties en 2021
* Mettez à jour la description du show `Kota Factory` avec la description suivante :
`In a city known for training India’s finest collegiate minds, an earnest but unexceptional student and his friends navigate campus life.`
* Choisissez un genre et affichez le.
* Supprimez `Jailbirds New Orleans`
* Affichez les titres et le casting.
* Regroupez les séries faisant partie de la catégorie `TV-MA`
* Comptez le nombre de séries par pays.
* Calculez le nombre de séries ajoutées à chaque année.
* Calculez le nombre de séries ajoutées à chaque année, et faisant partie de la catégorie `TV-MA`
* Une dernière requête en point bonus si vous le souhaitez, qui couvre la partie 7.

* (Attendu : Capture d'écran + CQL)

## 6. Conclusion

C'est à peu près tout ce qu'on peut faire sous Cassandra dans le cadre d'une base de données orientée colonne.