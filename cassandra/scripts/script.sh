#!/bin/bash
# définition de la clé primaire
PRIMARY_KEY='(title, country)' # Ici vous allez devoir modifier votre PRIMARY KEY à la volée
# création de la table
echo "création de la table"
cqlsh -k esgi_cassandra <<data
CREATE TABLE IF NOT EXISTS netflix_shows (
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
cqlsh -k esgi_cassandra <<data
COPY netflix_shows (
    title,
    cast,
    country,
    date_added,
    release_year,
    rating,
    duration,
    listed_in,
    description
) FROM 'output.csv' WITH HEADER = true;
data
# fin du script
