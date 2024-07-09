# TP 1

Anto Benedetti 3IABD2

## Parmi les éléments suivants, quel est celui que vous pouvez faire avec MongoDB Atlas ?

1. Stocker vos données avec le service mondial multi-cloud de MongoDB.
2. Ajouter une fonctionnalité de recherche à votre application, comme une barre de recherche.
4. Effectuer des requêtes sur plusieurs clusters Atlas pour obtenir une vue globale de vos données.

## Lesquelles des affirmations suivantes sont vraies à propos de MongoDB Atlas Clusters ?

1. Un cluster d’Atlas MongoDB est un groupe de serveurs connectés via un réseau qui contient des copies de vos données.
3. Les clusters MongoDB Atlas peuvent être déployés à l’échelle mondiale dans une seule région géographique ou dans plusieurs régions géographiques, en fonction du niveau de cluster.
4. Les clusters dédiés permettent d’accéder à toutes les fonctionnalités d’Atlas.

## Quelle commande permet de retourner le nom de la base de données ?

`db.getName()`

## Quelle commande permet de retourner le nom de toutes les collections contenues dans la base de données actuelle ?

`db.getCollectionNames()`

## Que se passe-t-il si l’on crée un utilisateur en doublon ?

La création échoue et une erreur est renvoyée, indiquant que l'utilisateur existe déjà.

## Testez la commande suivante db.adminCommand({listDatabases: 1}) : Que remarquez-vous ?

Il faut être authentifié pour pouvoir utiliser cette commande.

## Listez l’ensemble des bases de données qui sont disponible dans votre cluster local.

```console
admin> db.adminCommand({listDatabases: 1})
{
  databases: [
    { name: 'admin', sizeOnDisk: Long('102400'), empty: false },
    { name: 'config', sizeOnDisk: Long('12288'), empty: false },
    { name: 'local', sizeOnDisk: Long('73728'), empty: false }
  ],
  totalSize: Long('188416'),
  totalSizeMb: Long('0'),
  ok: 1
}
```

## Création du compte utilisateur pour les nouvelles BDD

```console
geospatial> db.createUser({
  user: "my-user1",
  pwd: "azerty123",
  roles: [
    { role: "readWrite", db: "geospatial" },
    { role: "read", db: "weather-data" }
  ]
})
```

Pour la première base de données, j'ai choisi le dossier "sample_geospatial" contenant une collection "shipwrecks", qui liste les naufrages de bateaux.
La deuxième est faite à partir du dossier "sample_weatherdata", contenant une collection "data", donnant la pression, la qualité de l'air, la température, etc de nombreux points géographiques.
