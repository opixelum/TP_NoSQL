#!/bin/bash
# définition de la clé primaire
PRIMARY_KEY='(titi, toto)' # Ici vous allez devoir modifier votre PRIMARY KEY à la volée
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