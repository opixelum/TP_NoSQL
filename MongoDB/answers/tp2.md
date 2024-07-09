# TP 2

Anto Benedetti 3IABD2

## 2.3. Au boulot

1. Donner les styles de cuisine présent dans la collection

```mongosh
db.restaurant.distinct("cuisine")
```

```console
[
  'Afghan',
  'African',
  'American ',
  'Armenian',
  'Asian',
  'Australian',
  'Bagels/Pretzels',
  'Bakery',
  'Bangladeshi',
  'Barbecue',
  'Bottled beverages, including water, sodas, juices, etc.',
  'Brazilian',
  'CafÃ©/Coffee/Tea',
  'Café/Coffee/Tea',
  'Cajun',
  'Californian',
  'Caribbean',
  'Chicken',
  'Chilean',
  'Chinese',
  'Chinese/Cuban',
  'Chinese/Japanese',
  'Continental',
  'Creole',
  'Creole/Cajun',
  'Czech',
  'Delicatessen',
  'Donuts',
  'Eastern European',
  'Egyptian',
  'English',
  'Ethiopian',
  'Filipino',
  'French',
  'Fruits/Vegetables',
  'German',
  'Greek',
  'Hamburgers',
  'Hawaiian',
  'Hotdogs',
  'Hotdogs/Pretzels',
  'Ice Cream, Gelato, Yogurt, Ices',
  'Indian',
  'Indonesian',
  'Iranian',
  'Irish',
  'Italian',
  'Japanese',
  'Jewish/Kosher',
  'Juice, Smoothies, Fruit Salads',
  'Korean',
  'Latin (Cuban, Dominican, Puerto Rican, South & Central American)',
  'Mediterranean',
  'Mexican',
  'Middle Eastern',
  'Moroccan',
  'Not Listed/Not Applicable',
  'Nuts/Confectionary',
  'Other',
  'Pakistani',
  'Pancakes/Waffles',
  'Peruvian',
  'Pizza',
  'Pizza/Italian',
  'Polish',
  'Polynesian',
  'Portuguese',
  'Russian',
  'Salads',
  'Sandwiches',
  'Sandwiches/Salads/Mixed Buffet',
  'Scandinavian',
  'Seafood',
  'Soul Food',
  'Soups',
  'Soups & Sandwiches',
  'Southwestern',
  'Spanish',
  'Steak',
  'Tapas',
  'Tex-Mex',
  'Thai',
  'Turkish',
  'Vegetarian',
  'Vietnamese/Cambodian/Malaysia'
]
```

2. Donner tous les grades possibles dans la base

```mongosh
db.restaurant.distinct("grades.grade")
```

```console
[ 'A', 'B', 'C', 'Not Yet Graded', 'P', 'Z' ]
```

3. Compter le nombre de restaurants proposant de la cuisine fraçaise (“French”)

```mongosh
db.restaurant.countDocuments({cuisine: "French"})
```

```console
344
```

4. Compter le nombre de restaurants situé sur la rue “Central Avenue”

```mongosh
db.restaurant.countDocuments({"address.street": "Central Avenue"})
```

```console
10
```

5. Compter le nombre de restaurants ayant eu une note supérieure à 50

```mongosh
db.restaurant.countDocuments({"grades.score": {$gt: 50}})
```

```console
349
```

6. Lister tous les restaurants, en n’aﬃchant que le nom, l’immeuble et la rue

```mongosh
db.restaurant.find({}, {name: 1, "address.building": 1, "address.street": 1, _id: 0})
```

```console
{
  address: {
    building: '1007',
    street: 'Morris Park Ave'
  },
  name: 'Morris Park Bake Shop'
}
{
  address: {
    building: '469',
    street: 'Flatbush Avenue'
  },
  name: "Wendy'S"
}
{
  address: {
    building: '351',
    street: 'West   57 Street'
  },
  name: 'Dj Reynolds Pub And Restaurant'
}
{
  address: {
    building: '2780',
    street: 'Stillwell Avenue'
  },
  name: 'Riviera Caterer'
}
{
  address: {
    building: '97-22',
    street: '63 Road'
  },
  name: 'Tov Kosher Kitchen'
}
{
  address: {
    building: '8825',
    street: 'Astoria Boulevard'
  },
  name: 'Brunos On The Boulevard'
}
{
  address: {
    building: '2206',
    street: 'Victory Boulevard'
  },
  name: 'Kosher Island'
}
{
  address: {
    building: '7114',
    street: 'Avenue U'
  },
  name: "Wilken'S Fine Food"
}
{
  address: {
    building: '6409',
    street: '11 Avenue'
  },
  name: 'Regina Caterers'
}
{
  address: {
    building: '1839',
    street: 'Nostrand Avenue'
  },
  name: 'Taste The Tropics Ice Cream'
}
{
  address: {
    building: '2300',
    street: 'Southern Boulevard'
  },
  name: 'Wild Asia'
}
{
  address: {
    building: '7715',
    street: '18 Avenue'
  },
  name: 'C & C Catering Service'
}
{
  address: {
    building: '1269',
    street: 'Sutter Avenue'
  },
  name: 'May May Kitchen'
}
{
  address: {
    building: '1',
    street: 'East   66 Street'
  },
  name: '1 East 66Th Street Kitchen'
}
{
  address: {
    building: '705',
    street: 'Kings Highway'
  },
  name: 'Seuda Foods'
}
{
  address: {
    building: '203',
    street: 'Church Avenue'
  },
  name: 'Carvel Ice Cream'
}
{
  address: {
    building: '265-15',
    street: 'Hillside Avenue'
  },
  name: 'Carvel Ice Cream'
}
{
  address: {
    building: '6909',
    street: '3 Avenue'
  },
  name: 'Nordic Delicacies'
}
{
  address: {
    building: '522',
    street: 'East   74 Street'
  },
  name: 'Glorious Food'
}
{
  address: {
    building: '284',
    street: 'Prospect Park West'
  },
  name: 'The Movable Feast'
}
Type "it" for more
```

7. Lister tous les restaurants nommés “Burger King” (nom et quartier uniquement)

```mongosh
db.restaurant.find({name: "Burger King"}, {name: 1, borough: 1, _id: 0})
```

```console
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Brooklyn',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Staten Island',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Queens',
  name: 'Burger King'
}
{
  borough: 'Bronx',
  name: 'Burger King'
}
{
  borough: 'Manhattan',
  name: 'Burger King'
}
{
  borough: 'Staten Island',
  name: 'Burger King'
}
{
  borough: 'Staten Island',
  name: 'Burger King'
}
{
  borough: 'Staten Island',
  name: 'Burger King'
}
{
  borough: 'Staten Island',
  name: 'Burger King'
}
{
  borough: 'Brooklyn',
  name: 'Burger King'
}
{
  borough: 'Brooklyn',
  name: 'Burger King'
}
{
  borough: 'Manhattan',
  name: 'Burger King'
}
Type "it" for more
```

8. Lister les restaurants situés sur les rues “Union Street” ou “Union Square”

```mongosh
db.restaurant.find({"address.street": {$in: ["Union Street", "Union Square"]}})
```

```console
{
  _id: ObjectId('668b230c4ef2b0950b9e68cf'),
  address: {
    building: '151',
    coord: [
      -74.00184349999999,
      40.684236
    ],
    street: 'Union Street',
    zipcode: '11231'
  },
  borough: 'Brooklyn',
  cuisine: 'Italian',
  grades: [
    {
      date: 2014-05-03T00:00:00.000Z,
      grade: 'A',
      score: 13
    },
    {
      date: 2013-04-23T00:00:00.000Z,
      grade: 'A',
      score: 12
    },
    {
      date: 2012-02-27T00:00:00.000Z,
      grade: 'A',
      score: 2
    }
  ],
  name: "Ferdinando'S Restaurant",
  restaurant_id: '40369716'
}
...
Tap "it" for more
```

9. Lister les restaurants situés au-dessus de la lattitude 40.90

```mongosh
db.restaurant.find({"address.coord.1": {$gt: 40.90}})
```

```console
{
  _id: ObjectId('668b230c4ef2b0950b9e68b4'),
  address: {
    building: '403416',
    coord: [
      -91.5971285,
      41.6823902
    ],
    street: '2Nd St',
    zipcode: '11358'
  },
  borough: 'Queens',
  cuisine: 'Café/Coffee/Tea',
  grades: [
    {
      date: 2014-04-16T00:00:00.000Z,
      grade: 'A',
      score: 11
    },
    {
      date: 2013-04-16T00:00:00.000Z,
      grade: 'A',
      score: 10
    },
    {
      date: 2012-04-17T00:00:00.000Z,
      grade: 'A',
      score: 10
    },
    {
      date: 2011-05-17T00:00:00.000Z,
      grade: 'A',
      score: 12
    }
  ],
  name: "Steve'S Coffee Shop",
  restaurant_id: '40369051'
}
...
Tap "it" for more
```

10. Lister les restaurants ayant eu un score de 0 et un grade “A”

```mongosh
db.restaurant.find({"grades": {$elemMatch: {score: 0, grade: "A"}}})
```

```console
{
  _id: ObjectId('668b230c4ef2b0950b9e67c7'),
  address: {
    building: '1',
    coord: [
      -73.96926909999999,
      40.7685235
    ],
    street: 'East   66 Street',
    zipcode: '10065'
  },
  borough: 'Manhattan',
  cuisine: 'American ',
  grades: [
    {
      date: 2014-05-07T00:00:00.000Z,
      grade: 'A',
      score: 3
    },
    {
      date: 2013-05-03T00:00:00.000Z,
      grade: 'A',
      score: 4
    },
    {
      date: 2012-04-30T00:00:00.000Z,
      grade: 'A',
      score: 6
    },
    {
      date: 2011-12-27T00:00:00.000Z,
      grade: 'A',
      score: 0
    }
  ],
  name: '1 East 66Th Street Kitchen',
  restaurant_id: '40359480'
}
...
Tap "it" for more
```

## 2.4. Allez dans le vrai terminal maintenant

1. Récupérer le ﬁchier users.json et l’importer dans la collection myUsers de la base test.

```console
mongoimport --host localhost:27017 --db test --collection myUsers < sample_data/users.json -u root -p example --authenticationDatabase admin
```

```console
2024-07-08T23:25:50.093-0400 connected to: mongodb://localhost:27017/
2024-07-08T23:25:50.252-0400 6998 document(s) imported successfully. 0 document(s) failed to import.
```

2. Finalement j’ai changé d’avis, je voulais l’importer dans la collection users. Supprimer la collection myUsers
   et réimporter dans la collection users,

```mongosh
db.myUsers.renameCollection("users")
```

```console
{ ok: 1 }
```

3. Utiliser le shell mongo pour compter le nombre d’éléments dans la collection users.

```mongosh
db.users.countDocuments()
```

```console
6998
```

4. Ajouter l’utilisateur dans la collection users

```mongosh
db.users.insertOne({
  name: "Chuck Norris",
  age: 77,
  hobbies: ["Karate", "Kung-fu", "Ruling the world"]
})
```

```console
{
  acknowledged: true,
  insertedId: ObjectId('668cafd551e1b0e365149f48')
}
```

5. Afficher Chuck Norris (si il le permet).

```mongosh
db.users.findOne({name: "Chuck Norris"})
```

```console
{
  _id: ObjectId('668cafd551e1b0e365149f48'),
  name: 'Chuck Norris',
  age: 77,
  hobbies: [ 'Karate', 'Kung-fu', 'Ruling the world' ]
}
```

6. Afficher Chuck sans le champs \_id.

```mongosh
db.users.findOne({name: "Chuck Norris"}, {_id: 0})
```

```console
{
  name: 'Chuck Norris',
  age: 77,
  hobbies: [ 'Karate', 'Kung-fu', 'Ruling the world' ]
}
```

7. Afficher les utilisateurs qui ont entre 20 et 25 ans.

```mongosh
db.users.find({age: {$gte: 20, $lte: 25}}).pretty()
```

```console
[
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8c9'),
    age: 23,
    name: 'Phillips Blake',
    gender: 'male',
    email: 'phillipsblake@retrack.com',
    phone: '+1 (883) 516-2545',
    address: {
      number: 370,
      street: 'Clara Street',
      city: 'Dale',
      state: 'Kansas',
      postal: 3257
    },
    favoriteFruit: 'peer',
    hobbies: [ 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d3'),
    age: 24,
    name: 'Vanessa Salas',
    gender: 'female',
    email: 'vanessasalas@retrack.com',
    phone: '+1 (976) 512-2318',
    address: {
      number: 818,
      street: 'Hoyts Lane',
      city: 'Brewster',
      state: 'Arkansas',
      postal: 6030
    },
    favoriteFruit: 'peer',
    hobbies: [ 'music', 'cooking', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d5'),
    age: 24,
    name: 'Jannie Frazier',
    gender: 'female',
    email: 'janniefrazier@retrack.com',
    phone: '+1 (819) 415-3085',
    address: {
      number: 331,
      street: 'Gerry Street',
      city: 'Taycheedah',
      state: 'Utah',
      postal: 9397
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'gaming', 'gaming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d6'),
    age: 22,
    name: 'Peggy Snider',
    gender: 'female',
    email: 'peggysnider@retrack.com',
    phone: '+1 (962) 493-2847',
    address: {
      number: 662,
      street: 'Conway Street',
      city: 'Clarktown',
      state: 'Connecticut',
      postal: 9927
    },
    favoriteFruit: 'banana',
    hobbies: [ 'computer science', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8db'),
    age: 25,
    name: 'Maribel Burns',
    gender: 'female',
    email: 'maribelburns@retrack.com',
    phone: '+1 (933) 577-3811',
    address: {
      number: 463,
      street: 'Hicks Street',
      city: 'Tivoli',
      state: 'Wisconsin',
      postal: 1413
    },
    favoriteFruit: 'banana',
    hobbies: [ 'poney', 'running', 'gaming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8e1'),
    age: 20,
    name: 'Atkins Maxwell',
    gender: 'male',
    email: 'atkinsmaxwell@retrack.com',
    phone: '+1 (826) 577-2430',
    address: {
      number: 385,
      street: 'Sullivan Street',
      city: 'Ronco',
      state: 'Louisiana',
      postal: 5337
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8e2'),
    age: 23,
    name: 'Ross Sanders',
    gender: 'male',
    email: 'rosssanders@retrack.com',
    phone: '+1 (911) 532-2919',
    address: {
      number: 804,
      street: 'Schenck Court',
      city: 'Cade',
      state: 'Minnesota',
      postal: 4805
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'theatre', 'theatre', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8e9'),
    age: 20,
    name: 'Shauna Wall',
    gender: 'female',
    email: 'shaunawall@retrack.com',
    phone: '+1 (844) 584-3535',
    address: {
      number: 229,
      street: 'Campus Road',
      city: 'Silkworth',
      state: 'Arizona',
      postal: 5463
    },
    favoriteFruit: 'apple',
    hobbies: [ 'poney', 'gaming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8f0'),
    age: 22,
    name: 'Sweet Robinson',
    gender: 'male',
    email: 'sweetrobinson@retrack.com',
    phone: '+1 (969) 501-3271',
    address: {
      number: 532,
      street: 'Nolans Lane',
      city: 'Cazadero',
      state: 'South Carolina',
      postal: 417
    },
    favoriteFruit: 'peer',
    hobbies: [ 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8f7'),
    age: 22,
    name: 'Gloria Ford',
    gender: 'female',
    email: 'gloriaford@retrack.com',
    phone: '+1 (870) 595-3601',
    address: {
      number: 875,
      street: 'Marconi Place',
      city: 'Adelino',
      state: 'Maryland',
      postal: 3934
    },
    favoriteFruit: 'peer',
    hobbies: [ 'reading', 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e906'),
    age: 24,
    name: 'Jeanine Whitehead',
    gender: 'female',
    email: 'jeaninewhitehead@retrack.com',
    phone: '+1 (923) 462-3380',
    address: {
      number: 256,
      street: 'Hendrix Street',
      city: 'Blairstown',
      state: 'Arkansas',
      postal: 5105
    },
    favoriteFruit: 'apple',
    hobbies: [ 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e90f'),
    age: 25,
    name: 'Karen Glenn',
    gender: 'female',
    email: 'karenglenn@retrack.com',
    phone: '+1 (978) 561-2509',
    address: {
      number: 313,
      street: 'Holly Street',
      city: 'Guthrie',
      state: 'Rhode Island',
      postal: 9751
    },
    favoriteFruit: 'banana',
    hobbies: [ 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e91b'),
    age: 23,
    name: 'Oliver Pugh',
    gender: 'male',
    email: 'oliverpugh@retrack.com',
    phone: '+1 (973) 585-2791',
    address: {
      number: 935,
      street: 'Chester Court',
      city: 'Caberfae',
      state: 'Washington',
      postal: 2889
    },
    favoriteFruit: 'peer',
    hobbies: [ 'reading', 'music', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e91c'),
    age: 23,
    name: 'Johns Briggs',
    gender: 'male',
    email: 'johnsbriggs@retrack.com',
    phone: '+1 (841) 488-2773',
    address: {
      number: 255,
      street: 'Prospect Avenue',
      city: 'Woodruff',
      state: 'Oklahoma',
      postal: 469
    },
    favoriteFruit: 'peer',
    hobbies: [ 'theatre', 'running', 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e924'),
    age: 20,
    name: 'Patrice Mann',
    gender: 'female',
    email: 'patricemann@retrack.com',
    phone: '+1 (994) 402-3561',
    address: {
      number: 591,
      street: 'Hendrickson Street',
      city: 'Wauhillau',
      state: 'Massachusetts',
      postal: 2158
    },
    favoriteFruit: 'banana',
    hobbies: [ 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e927'),
    age: 24,
    name: 'Holly Bates',
    gender: 'female',
    email: 'hollybates@retrack.com',
    phone: '+1 (934) 558-3840',
    address: {
      number: 334,
      street: 'Madoc Avenue',
      city: 'Fillmore',
      state: 'Florida',
      postal: 8960
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e928'),
    age: 25,
    name: 'Alicia Mcguire',
    gender: 'female',
    email: 'aliciamcguire@retrack.com',
    phone: '+1 (812) 477-2561',
    address: {
      number: 546,
      street: 'Bushwick Avenue',
      city: 'Wanamie',
      state: 'Mississippi',
      postal: 5311
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'swimming', 'poney' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e94d'),
    age: 20,
    name: 'Hillary Warner',
    gender: 'female',
    email: 'hillarywarner@retrack.com',
    phone: '+1 (863) 410-3306',
    address: {
      number: 812,
      street: 'Bokee Court',
      city: 'Edinburg',
      state: 'Indiana',
      postal: 5493
    },
    favoriteFruit: 'apple',
    hobbies: [ 'theatre', 'gaming', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e953'),
    age: 21,
    name: 'Tasha Hale',
    gender: 'female',
    email: 'tashahale@retrack.com',
    phone: '+1 (830) 539-3481',
    address: {
      number: 944,
      street: 'Claver Place',
      city: 'Rivereno',
      state: 'Washington',
      postal: 5030
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'cinema', 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e955'),
    age: 24,
    name: 'Brooks Huffman',
    gender: 'male',
    email: 'brookshuffman@retrack.com',
    phone: '+1 (861) 474-2856',
    address: {
      number: 288,
      street: 'Orange Street',
      city: 'Bonanza',
      state: 'Oklahoma',
      postal: 160
    },
    favoriteFruit: 'peer',
    hobbies: [ 'swimming', 'cinema' ]
  }
]
Type "it" for more
```

8. Afficher uniquement les hommes entre 30 et 40 ans.

```mongosh
db.users.find({age: {$gte: 30, $lte: 40}, gender: "male"}).pretty()
```

```console
[
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8cf'),
    age: 33,
    name: 'Cameron Cline',
    gender: 'male',
    email: 'cameroncline@retrack.com',
    phone: '+1 (931) 425-3324',
    address: {
      number: 870,
      street: 'Johnson Street',
      city: 'Thomasville',
      state: 'Nevada',
      postal: 1151
    },
    favoriteFruit: 'peer',
    hobbies: [ 'gaming', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8ec'),
    age: 37,
    name: 'Quinn Lott',
    gender: 'male',
    email: 'quinnlott@retrack.com',
    phone: '+1 (897) 596-2052',
    address: {
      number: 509,
      street: 'Cypress Court',
      city: 'Ticonderoga',
      state: 'Hawaii',
      postal: 6056
    },
    favoriteFruit: 'peer',
    hobbies: [ 'cinema', 'poney', 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8ef'),
    age: 34,
    name: 'Lynn Prince',
    gender: 'male',
    email: 'lynnprince@retrack.com',
    phone: '+1 (927) 504-3081',
    address: {
      number: 471,
      street: 'Holmes Lane',
      city: 'Escondida',
      state: 'South Dakota',
      postal: 6559
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'swimming', 'cinema', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8f4'),
    age: 37,
    name: 'Hebert Sherman',
    gender: 'male',
    email: 'hebertsherman@retrack.com',
    phone: '+1 (916) 453-2992',
    address: {
      number: 907,
      street: 'Landis Court',
      city: 'Haena',
      state: 'Montana',
      postal: 9332
    },
    favoriteFruit: 'banana',
    hobbies: [ 'theatre', 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8fa'),
    age: 39,
    name: 'Dudley Stokes',
    gender: 'male',
    email: 'dudleystokes@retrack.com',
    phone: '+1 (961) 597-3360',
    address: {
      number: 949,
      street: 'Butler Place',
      city: 'Talpa',
      state: 'Alabama',
      postal: 6496
    },
    favoriteFruit: 'banana',
    hobbies: [ 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e904'),
    age: 30,
    name: 'Higgins Battle',
    gender: 'male',
    email: 'higginsbattle@retrack.com',
    phone: '+1 (826) 563-3870',
    address: {
      number: 138,
      street: 'Dean Street',
      city: 'Farmington',
      state: 'Michigan',
      postal: 5963
    },
    favoriteFruit: 'peer',
    hobbies: [ 'reading', 'gaming', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e905'),
    age: 40,
    name: 'Strickland Schmidt',
    gender: 'male',
    email: 'stricklandschmidt@retrack.com',
    phone: '+1 (897) 581-3754',
    address: {
      number: 669,
      street: 'Lorimer Street',
      city: 'Malott',
      state: 'North Dakota',
      postal: 6019
    },
    favoriteFruit: 'peer',
    hobbies: [ 'reading', 'theatre', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e91e'),
    age: 40,
    name: 'Bruce Mclaughlin',
    gender: 'male',
    email: 'brucemclaughlin@retrack.com',
    phone: '+1 (961) 535-2655',
    address: {
      number: 833,
      street: 'Temple Court',
      city: 'Fairforest',
      state: 'Hawaii',
      postal: 5019
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'cooking', 'gaming', 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e937'),
    age: 37,
    name: 'Zimmerman Kent',
    gender: 'male',
    email: 'zimmermankent@retrack.com',
    phone: '+1 (976) 403-2265',
    address: {
      number: 604,
      street: 'Montana Place',
      city: 'Trucksville',
      state: 'Tennessee',
      postal: 1679
    },
    favoriteFruit: 'peer',
    hobbies: [ 'computer science' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e93c'),
    age: 36,
    name: 'Turner Patton',
    gender: 'male',
    email: 'turnerpatton@retrack.com',
    phone: '+1 (966) 528-2753',
    address: {
      number: 906,
      street: 'Tampa Court',
      city: 'Makena',
      state: 'Georgia',
      postal: 2259
    },
    favoriteFruit: 'banana',
    hobbies: [ 'music', 'computer science', 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e946'),
    age: 35,
    name: 'Barber Hewitt',
    gender: 'male',
    email: 'barberhewitt@retrack.com',
    phone: '+1 (892) 563-2846',
    address: {
      number: 759,
      street: 'Greenpoint Avenue',
      city: 'Darbydale',
      state: 'Arkansas',
      postal: 4753
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e952'),
    age: 37,
    name: 'Osborne Levine',
    gender: 'male',
    email: 'osbornelevine@retrack.com',
    phone: '+1 (905) 499-3578',
    address: {
      number: 190,
      street: 'Hudson Avenue',
      city: 'Benson',
      state: 'Iowa',
      postal: 3009
    },
    favoriteFruit: 'apple',
    hobbies: [ 'cooking' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e95e'),
    age: 39,
    name: 'Morton Hoffman',
    gender: 'male',
    email: 'mortonhoffman@retrack.com',
    phone: '+1 (822) 412-3323',
    address: {
      number: 379,
      street: 'Hancock Street',
      city: 'Blanford',
      state: 'Massachusetts',
      postal: 1723
    },
    favoriteFruit: 'peer',
    hobbies: [ 'gaming', 'cinema', 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e964'),
    age: 34,
    name: 'Wilson Owens',
    gender: 'male',
    email: 'wilsonowens@retrack.com',
    phone: '+1 (831) 542-3859',
    address: {
      number: 700,
      street: 'Bevy Court',
      city: 'Falconaire',
      state: 'Virginia',
      postal: 2152
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'cinema', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e96b'),
    age: 32,
    name: 'Macdonald Holmes',
    gender: 'male',
    email: 'macdonaldholmes@retrack.com',
    phone: '+1 (943) 525-2665',
    address: {
      number: 771,
      street: 'Cortelyou Road',
      city: 'Turah',
      state: 'North Dakota',
      postal: 7161
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'theatre', 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e975'),
    age: 33,
    name: 'Rodgers Langley',
    gender: 'male',
    email: 'rodgerslangley@retrack.com',
    phone: '+1 (901) 504-3325',
    address: {
      number: 795,
      street: 'Box Street',
      city: 'Balm',
      state: 'Oregon',
      postal: 646
    },
    favoriteFruit: 'peer',
    hobbies: [ 'cinema', 'poney' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e97b'),
    age: 31,
    name: 'Simon Adams',
    gender: 'male',
    email: 'simonadams@retrack.com',
    phone: '+1 (879) 457-3617',
    address: {
      number: 458,
      street: 'Turner Place',
      city: 'Frierson',
      state: 'Mississippi',
      postal: 9520
    },
    favoriteFruit: 'apple',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e98d'),
    age: 38,
    name: 'Randolph York',
    gender: 'male',
    email: 'randolphyork@retrack.com',
    phone: '+1 (858) 428-3709',
    address: {
      number: 890,
      street: 'Benson Avenue',
      city: 'Fidelis',
      state: 'Washington',
      postal: 6987
    },
    favoriteFruit: 'banana',
    hobbies: [ 'poney', 'gaming', 'computer science' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e991'),
    age: 33,
    name: 'Vang Bryan',
    gender: 'male',
    email: 'vangbryan@retrack.com',
    phone: '+1 (989) 458-3730',
    address: {
      number: 377,
      street: 'Nautilus Avenue',
      city: 'Muir',
      state: 'South Carolina',
      postal: 6022
    },
    favoriteFruit: 'banana',
    hobbies: [ 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e9a5'),
    age: 32,
    name: 'Wilcox Peterson',
    gender: 'male',
    email: 'wilcoxpeterson@retrack.com',
    phone: '+1 (952) 594-3133',
    address: {
      number: 454,
      street: 'Linwood Street',
      city: 'Callaghan',
      state: 'Wyoming',
      postal: 9772
    },
    favoriteFruit: 'apple',
    hobbies: [ 'theatre', 'kung-fu', 'cooking' ]
  }
]
Type "it" for more
```

9. Afficher les utilisateurs habitant l’état de Louisianne (Louisiana)

```mongosh
db.users.find({"address.state": "Louisiana"}).pretty()
```

```console
[
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8e1'),
    age: 20,
    name: 'Atkins Maxwell',
    gender: 'male',
    email: 'atkinsmaxwell@retrack.com',
    phone: '+1 (826) 577-2430',
    address: {
      number: 385,
      street: 'Sullivan Street',
      city: 'Ronco',
      state: 'Louisiana',
      postal: 5337
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e914'),
    age: 44,
    name: 'Dickerson Simmons',
    gender: 'male',
    email: 'dickersonsimmons@retrack.com',
    phone: '+1 (961) 564-3949',
    address: {
      number: 528,
      street: 'Sullivan Place',
      city: 'Bradenville',
      state: 'Louisiana',
      postal: 3891
    },
    favoriteFruit: 'apple',
    hobbies: [ 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e92e'),
    age: 31,
    name: 'Kim Hodge',
    gender: 'female',
    email: 'kimhodge@retrack.com',
    phone: '+1 (918) 414-2326',
    address: {
      number: 579,
      street: 'Bergen Place',
      city: 'Waverly',
      state: 'Louisiana',
      postal: 7033
    },
    favoriteFruit: 'peer',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e96c'),
    age: 59,
    name: 'Pacheco Skinner',
    gender: 'male',
    email: 'pachecoskinner@retrack.com',
    phone: '+1 (900) 514-3021',
    address: {
      number: 981,
      street: 'Stryker Court',
      city: 'Urie',
      state: 'Louisiana',
      postal: 4940
    },
    favoriteFruit: 'banana',
    hobbies: [ 'swimming', 'cinema', 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e99b'),
    age: 44,
    name: 'Nash Diaz',
    gender: 'male',
    email: 'nashdiaz@retrack.com',
    phone: '+1 (958) 441-3701',
    address: {
      number: 521,
      street: 'Bridgewater Street',
      city: 'Fontanelle',
      state: 'Louisiana',
      postal: 6611
    },
    favoriteFruit: 'peer',
    hobbies: [ 'kung-fu', 'computer science', 'reading' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e9c7'),
    age: 18,
    name: 'Jackie Finch',
    gender: 'female',
    email: 'jackiefinch@retrack.com',
    phone: '+1 (848) 485-3546',
    address: {
      number: 990,
      street: 'Caton Avenue',
      city: 'Indio',
      state: 'Louisiana',
      postal: 7437
    },
    favoriteFruit: 'peer',
    hobbies: [ 'cooking', 'cooking', 'computer science' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e9fa'),
    age: 21,
    name: 'Joy England',
    gender: 'female',
    email: 'joyengland@retrack.com',
    phone: '+1 (993) 510-3638',
    address: {
      number: 459,
      street: 'Jardine Place',
      city: 'Dupuyer',
      state: 'Louisiana',
      postal: 7243
    },
    favoriteFruit: 'banana',
    hobbies: [ 'cinema', 'poney' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea2b'),
    age: 31,
    name: 'Marcy Walter',
    gender: 'female',
    email: 'marcywalter@retrack.com',
    phone: '+1 (922) 519-3281',
    address: {
      number: 669,
      street: 'Columbia Place',
      city: 'Edneyville',
      state: 'Louisiana',
      postal: 801
    },
    favoriteFruit: 'apple',
    hobbies: [ 'gaming', 'theatre', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea5d'),
    age: 60,
    name: 'Dollie Espinoza',
    gender: 'female',
    email: 'dollieespinoza@retrack.com',
    phone: '+1 (823) 600-3053',
    address: {
      number: 523,
      street: 'Poplar Avenue',
      city: 'Kempton',
      state: 'Louisiana',
      postal: 4738
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'reading' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea91'),
    age: 29,
    name: 'Jayne Rush',
    gender: 'female',
    email: 'jaynerush@retrack.com',
    phone: '+1 (817) 513-3594',
    address: {
      number: 595,
      street: 'Lincoln Avenue',
      city: 'Welda',
      state: 'Louisiana',
      postal: 7470
    },
    favoriteFruit: 'apple',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eabc'),
    age: 22,
    name: 'Yesenia Garza',
    gender: 'female',
    email: 'yeseniagarza@retrack.com',
    phone: '+1 (954) 558-2485',
    address: {
      number: 273,
      street: 'Montague Street',
      city: 'Avalon',
      state: 'Louisiana',
      postal: 6646
    },
    favoriteFruit: 'banana',
    hobbies: [ 'cooking', 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eaef'),
    age: 55,
    name: 'Cook Howard',
    gender: 'male',
    email: 'cookhoward@retrack.com',
    phone: '+1 (947) 550-3320',
    address: {
      number: 362,
      street: 'Coleman Street',
      city: 'Corinne',
      state: 'Louisiana',
      postal: 4837
    },
    favoriteFruit: 'peer',
    hobbies: [ 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb1e'),
    age: 25,
    name: 'Figueroa Mcclain',
    gender: 'male',
    email: 'figueroamcclain@retrack.com',
    phone: '+1 (811) 539-3271',
    address: {
      number: 286,
      street: 'Jerome Street',
      city: 'Nettie',
      state: 'Louisiana',
      postal: 9329
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb53'),
    age: 53,
    name: 'Vincent Nichols',
    gender: 'male',
    email: 'vincentnichols@retrack.com',
    phone: '+1 (808) 536-3867',
    address: {
      number: 505,
      street: 'Tompkins Avenue',
      city: 'Noblestown',
      state: 'Louisiana',
      postal: 4063
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'cooking' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb81'),
    age: 33,
    name: 'Blake Mccarty',
    gender: 'male',
    email: 'blakemccarty@retrack.com',
    phone: '+1 (844) 548-2241',
    address: {
      number: 316,
      street: 'Schenck Street',
      city: 'Enetai',
      state: 'Louisiana',
      postal: 8275
    },
    favoriteFruit: 'peer',
    hobbies: [ 'gaming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ebb1'),
    age: 47,
    name: 'Katie Shannon',
    gender: 'female',
    email: 'katieshannon@retrack.com',
    phone: '+1 (818) 587-3861',
    address: {
      number: 928,
      street: 'Maple Street',
      city: 'Brantleyville',
      state: 'Louisiana',
      postal: 2301
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'reading', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ebda'),
    age: 13,
    name: 'Diann Ewing',
    gender: 'female',
    email: 'diannewing@retrack.com',
    phone: '+1 (944) 507-2320',
    address: {
      number: 906,
      street: 'Coffey Street',
      city: 'Hanover',
      state: 'Louisiana',
      postal: 5377
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'cooking' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ec15'),
    age: 13,
    name: 'Angel Snow',
    gender: 'female',
    email: 'angelsnow@retrack.com',
    phone: '+1 (982) 555-2003',
    address: {
      number: 585,
      street: 'Willow Street',
      city: 'Aurora',
      state: 'Louisiana',
      postal: 4666
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'gaming', 'swimming', 'reading' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ec41'),
    age: 55,
    name: 'Holloway Hopkins',
    gender: 'male',
    email: 'hollowayhopkins@retrack.com',
    phone: '+1 (805) 497-3352',
    address: {
      number: 968,
      street: 'Brooklyn Road',
      city: 'Chautauqua',
      state: 'Louisiana',
      postal: 3717
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ec77'),
    age: 15,
    name: 'Horne Beach',
    gender: 'male',
    email: 'hornebeach@retrack.com',
    phone: '+1 (835) 494-2084',
    address: {
      number: 613,
      street: 'Sapphire Street',
      city: 'Tonopah',
      state: 'Louisiana',
      postal: 9386
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'reading', 'swimming' ]
  }
]
Type "it" for more
```

10. Afficher les 20 premiers utilisateurs triés par ordre décroissant d’age.

```mongosh
db.users.find().sort({age: -1}).limit(20).pretty()
```

```console
[
  {
    _id: ObjectId('668cafd551e1b0e365149f48'),
    name: 'Chuck Norris',
    age: 77,
    hobbies: [ 'Karate', 'Kung-fu', 'Ruling the world' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb28'),
    age: 60,
    name: 'Chrystal Booth',
    gender: 'female',
    email: 'chrystalbooth@retrack.com',
    phone: '+1 (844) 447-3503',
    address: {
      number: 876,
      street: 'Lawrence Street',
      city: 'Biddle',
      state: 'New Mexico',
      postal: 3403
    },
    favoriteFruit: 'banana',
    hobbies: [ 'swimming', 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e909'),
    age: 60,
    name: 'Sutton Stephenson',
    gender: 'male',
    email: 'suttonstephenson@retrack.com',
    phone: '+1 (804) 517-3754',
    address: {
      number: 693,
      street: 'Montague Terrace',
      city: 'Weedville',
      state: 'Wyoming',
      postal: 399
    },
    favoriteFruit: 'peer',
    hobbies: [ 'swimming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea6e'),
    age: 60,
    name: 'Hardin Conrad',
    gender: 'male',
    email: 'hardinconrad@retrack.com',
    phone: '+1 (894) 536-2685',
    address: {
      number: 641,
      street: 'Sackman Street',
      city: 'Carlton',
      state: 'Missouri',
      postal: 1660
    },
    favoriteFruit: 'apple',
    hobbies: [ 'swimming', 'theatre', 'theatre' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ebe4'),
    age: 60,
    name: 'Delia Stark',
    gender: 'female',
    email: 'deliastark@retrack.com',
    phone: '+1 (923) 438-2629',
    address: {
      number: 297,
      street: 'Carlton Avenue',
      city: 'Lawrence',
      state: 'New Hampshire',
      postal: 6558
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'gaming', 'poney' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb68'),
    age: 60,
    name: 'Madelyn Nguyen',
    gender: 'female',
    email: 'madelynnguyen@retrack.com',
    phone: '+1 (882) 536-3474',
    address: {
      number: 885,
      street: 'Bush Street',
      city: 'Osmond',
      state: 'Kentucky',
      postal: 1792
    },
    favoriteFruit: 'banana',
    hobbies: [ 'theatre', 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eb15'),
    age: 60,
    name: 'Clayton Mullen',
    gender: 'male',
    email: 'claytonmullen@retrack.com',
    phone: '+1 (826) 574-3672',
    address: {
      number: 897,
      street: 'Cass Place',
      city: 'Cawood',
      state: 'Alabama',
      postal: 7299
    },
    favoriteFruit: 'apple',
    hobbies: [ 'theatre', 'swimming', 'gaming' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ed47'),
    age: 60,
    name: 'Livingston Smith',
    gender: 'male',
    email: 'livingstonsmith@retrack.com',
    phone: '+1 (833) 424-2283',
    address: {
      number: 315,
      street: 'Hornell Loop',
      city: 'Fairhaven',
      state: 'Michigan',
      postal: 7110
    },
    favoriteFruit: 'peer',
    hobbies: [ 'computer science' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea76'),
    age: 60,
    name: 'Alexandra Wilkinson',
    gender: 'female',
    email: 'alexandrawilkinson@retrack.com',
    phone: '+1 (917) 574-2733',
    address: {
      number: 822,
      street: 'Desmond Court',
      city: 'Sunwest',
      state: 'West Virginia',
      postal: 2444
    },
    favoriteFruit: 'apple',
    hobbies: [ 'kung-fu', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8df'),
    age: 60,
    name: 'Myrtle Becker',
    gender: 'female',
    email: 'myrtlebecker@retrack.com',
    phone: '+1 (812) 412-2219',
    address: {
      number: 282,
      street: 'Clarendon Road',
      city: 'Bennett',
      state: 'Idaho',
      postal: 5745
    },
    favoriteFruit: 'peer',
    hobbies: [ 'running', 'computer science', 'cooking' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8e0'),
    age: 60,
    name: 'Jeannine Haney',
    gender: 'female',
    email: 'jeanninehaney@retrack.com',
    phone: '+1 (870) 500-2530',
    address: {
      number: 378,
      street: 'Elton Street',
      city: 'Keller',
      state: 'Maine',
      postal: 3785
    },
    favoriteFruit: 'banana',
    hobbies: [ 'poney', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ebfa'),
    age: 60,
    name: 'Daphne Larson',
    gender: 'female',
    email: 'daphnelarson@retrack.com',
    phone: '+1 (869) 460-2276',
    address: {
      number: 244,
      street: 'Doscher Street',
      city: 'Sterling',
      state: 'Georgia',
      postal: 5675
    },
    favoriteFruit: 'apple',
    hobbies: [ 'reading', 'gaming', 'cooking' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ed32'),
    age: 60,
    name: 'Annmarie Brennan',
    gender: 'female',
    email: 'annmariebrennan@retrack.com',
    phone: '+1 (821) 422-3462',
    address: {
      number: 932,
      street: 'Wythe Place',
      city: 'Loomis',
      state: 'Florida',
      postal: 4734
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'poney', 'swimming', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea5d'),
    age: 60,
    name: 'Dollie Espinoza',
    gender: 'female',
    email: 'dollieespinoza@retrack.com',
    phone: '+1 (823) 600-3053',
    address: {
      number: 523,
      street: 'Poplar Avenue',
      city: 'Kempton',
      state: 'Louisiana',
      postal: 4738
    },
    favoriteFruit: 'strawberry',
    hobbies: [ 'running', 'reading' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ed3a'),
    age: 60,
    name: 'Dianne Velez',
    gender: 'female',
    email: 'diannevelez@retrack.com',
    phone: '+1 (802) 567-3229',
    address: {
      number: 434,
      street: 'Hubbard Place',
      city: 'Caroleen',
      state: 'New Jersey',
      postal: 8502
    },
    favoriteFruit: 'apple',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea1a'),
    age: 60,
    name: 'Bianca Sims',
    gender: 'female',
    email: 'biancasims@retrack.com',
    phone: '+1 (995) 534-3237',
    address: {
      number: 865,
      street: 'Carroll Street',
      city: 'Manila',
      state: 'South Dakota',
      postal: 1204
    },
    favoriteFruit: 'peer',
    hobbies: [ 'cooking', 'cinema' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6edcf'),
    age: 60,
    name: 'Hull Kidd',
    gender: 'male',
    email: 'hullkidd@retrack.com',
    phone: '+1 (816) 584-2442',
    address: {
      number: 558,
      street: 'Vermont Street',
      city: 'Kenmar',
      state: 'New York',
      postal: 187
    },
    favoriteFruit: 'peer',
    hobbies: [ 'music' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6edce'),
    age: 60,
    name: 'Reeves Thompson',
    gender: 'male',
    email: 'reevesthompson@retrack.com',
    phone: '+1 (802) 448-2512',
    address: {
      number: 671,
      street: 'Douglass Street',
      city: 'Chesterfield',
      state: 'Pennsylvania',
      postal: 6089
    },
    favoriteFruit: 'banana',
    hobbies: [ 'running' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6eac4'),
    age: 60,
    name: 'Hickman Branch',
    gender: 'male',
    email: 'hickmanbranch@retrack.com',
    phone: '+1 (919) 522-3586',
    address: {
      number: 681,
      street: 'Saratoga Avenue',
      city: 'Ypsilanti',
      state: 'Pennsylvania',
      postal: 1702
    },
    favoriteFruit: 'banana',
    hobbies: [ 'theatre', 'kung-fu' ]
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6ea79'),
    age: 60,
    name: 'Watson Beasley',
    gender: 'male',
    email: 'watsonbeasley@retrack.com',
    phone: '+1 (816) 486-2247',
    address: {
      number: 530,
      street: 'Downing Street',
      city: 'Bendon',
      state: 'Oklahoma',
      postal: 8660
    },
    favoriteFruit: 'banana',
    hobbies: [ 'theatre' ]
  }
]
Type "it" for more
```

11. Combien y’a-t-il de femmes agées de 30 ans?

```mongosh
db.users.countDocuments({age: 30, gender: "female"})
```

```console
63
```

12. Nos juristes nous ont dit que nous ne pouvions plus garder les numéro de téléphones de nos utilisateurs :
    supprimer le champ phone de tous les enregistrements.

```mongosh
db.users.updateMany({}, {$unset: {phone: ""}})
```

```console
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 6999,
  modifiedCount: 6998,
  upsertedCount: 0
}
```

13. Chuck Norris est venu nous dire que le temps ne marquait pas Chuck Norris, mais que Chuck Norris mar-
    quait le temps : changer l’age de Chuck Norris à infinity

```mongosh
db.users.updateOne({name: "Chuck Norris"}, {$set: {age: "infinity"}})
```

```console
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

14. Ajoutons un hobby à tous nos utilisateurs de plus de 50 ans : jardinage

```mongosh
db.users.updateMany({age: {$gt: 50}}, {$push: {hobbies: "jardinage"}})
```

```console
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1391,
  modifiedCount: 1391,
  upsertedCount: 0
}
```

15. Je souhaite savoir combien d’utilisateur j’ai dans chaque état, lister les états en indiquant pour chacun, le
    nombre d’utilisateurs présents.

```mongosh
db.users.aggregate([
  {$group: {_id: "$address.state", count: {$sum: 1}}}
])
```

```console
[
  { _id: 'Delaware', count: 143 },
  { _id: 'Rhode Island', count: 143 },
  { _id: 'Utah', count: 143 },
  { _id: 'Michigan', count: 143 },
  { _id: 'Iowa', count: 142 },
  { _id: 'Connecticut', count: 143 },
  { _id: 'Idaho', count: 143 },
  { _id: 'West Virginia', count: 143 },
  { _id: 'Pennsylvania', count: 143 },
  { _id: 'Indiana', count: 143 },
  { _id: 'Oklahoma', count: 142 },
  { _id: 'Illinois', count: 143 },
  { _id: 'Kansas', count: 143 },
  { _id: 'Alaska', count: 143 },
  { _id: 'North Carolina', count: 143 },
  { _id: 'Montana', count: 143 },
  { _id: 'South Dakota', count: 142 },
  { _id: 'Arkansas', count: 143 },
  { _id: 'Nevada', count: 143 },
  { _id: 'Oregon', count: 143 }
]
Type "it" for more
```

16. Je souhaite savoir l’âge moyen des utilisateurs de chaque état.

```mongosh
db.users.aggregate([
  {$group: {_id: "$address.state", avgAge: {$avg: "$age"}}}
])
```

```console
[
  { _id: 'Delaware', avgAge: 34.3986013986014 },
  { _id: 'Rhode Island', avgAge: 35.32167832167832 },
  { _id: 'Utah', avgAge: 34.79020979020979 },
  { _id: 'Michigan', avgAge: 32.75524475524475 },
  { _id: 'Iowa', avgAge: 36.267605633802816 },
  { _id: 'Connecticut', avgAge: 33.35664335664335 },
  { _id: 'Idaho', avgAge: 35.25874125874126 },
  { _id: 'West Virginia', avgAge: 35.85314685314685 },
  { _id: 'Pennsylvania', avgAge: 35.37762237762238 },
  { _id: 'Indiana', avgAge: 35.95804195804196 },
  { _id: 'Oklahoma', avgAge: 34.36619718309859 },
  { _id: 'Illinois', avgAge: 33.49650349650349 },
  { _id: 'Kansas', avgAge: 33.72727272727273 },
  { _id: 'Alaska', avgAge: 34.86013986013986 },
  { _id: 'North Carolina', avgAge: 35.29370629370629 },
  { _id: 'Montana', avgAge: 34.97902097902098 },
  { _id: 'South Dakota', avgAge: 34.021126760563384 },
  { _id: 'Arkansas', avgAge: 36.72727272727273 },
  { _id: 'Nevada', avgAge: 36.55944055944056 },
  { _id: 'Oregon', avgAge: 36.38461538461539 }
]
Type "it" for more
```

17. Je veux connaître la liste de tous les hobbies de chaque ville.

```mongosh
db.users.aggregate([
  {$unwind: "$hobbies"},
  {$group: {_id: "$address.city", hobbies: {$addToSet: "$hobbies"}}}
])
```

```console
[
  {
    _id: 'Rosburg',
    hobbies: [
      'kung-fu',
      'computer science',
      'theatre',
      'music',
      'gaming',
      'cooking',
      'jardinage',
      'reading',
      'swimming'
    ]
  },
  {
    _id: 'Neahkahnie',
    hobbies: [
      'cinema',
      'theatre',
      'jardinage',
      'gaming',
      'reading',
      'swimming',
      'kung-fu',
      'computer science',
      'poney',
      'music'
    ]
  },
  {
    _id: 'Cloverdale',
    hobbies: [
      'gaming',  'jardinage',
      'theatre', 'music',
      'reading', 'swimming',
      'poney',   'cooking'
    ]
  },
  {
    _id: 'Blue',
    hobbies: [
      'kung-fu',
      'poney',
      'computer science',
      'running',
      'theatre',
      'cinema',
      'jardinage',
      'gaming',
      'music',
      'cooking',
      'swimming'
    ]
  },
  {
    _id: 'Starks',
    hobbies: [
      'running',
      'computer science',
      'poney',
      'kung-fu',
      'gaming',
      'cinema',
      'music',
      'theatre',
      'jardinage',
      'reading'
    ]
  },
  {
    _id: 'Teasdale',
    hobbies: [ 'music', 'theatre', 'reading', 'cinema', 'swimming', 'kung-fu' ]
  },
  {
    _id: 'Graball',
    hobbies: [
      'music',    'theatre',
      'kung-fu',  'cooking',
      'cinema',   'poney',
      'swimming', 'jardinage'
    ]
  },
  {
    _id: 'Carrsville',
    hobbies: [
      'music',
      'cinema',
      'computer science',
      'swimming',
      'reading',
      'poney',
      'running',
      'kung-fu',
      'theatre',
      'cooking',
      'gaming'
    ]
  },
  {
    _id: 'Virgie',
    hobbies: [
      'reading',
      'poney',
      'computer science',
      'running',
      'theatre',
      'music',
      'gaming',
      'cooking',
      'jardinage',
      'swimming'
    ]
  },
  {
    _id: 'Brambleton',
    hobbies: [
      'running',
      'poney',
      'computer science',
      'swimming',
      'theatre',
      'jardinage',
      'cinema',
      'cooking',
      'music',
      'kung-fu',
      'gaming'
    ]
  },
  {
    _id: 'Springdale',
    hobbies: [
      'gaming',    'theatre',
      'cooking',   'kung-fu',
      'running',   'poney',
      'music',     'swimming',
      'jardinage'
    ]
  },
  {
    _id: 'Morningside',
    hobbies: [
      'cinema',
      'cooking',
      'theatre',
      'poney',
      'computer science',
      'swimming',
      'reading',
      'jardinage'
    ]
  },
  {
    _id: 'Highland',
    hobbies: [
      'computer science',
      'reading',
      'running',
      'poney',
      'jardinage',
      'theatre',
      'gaming',
      'cooking',
      'kung-fu',
      'cinema'
    ]
  },
  {
    _id: 'Osage',
    hobbies: [
      'computer science',
      'running',
      'kung-fu',
      'reading',
      'gaming',
      'cooking',
      'swimming'
    ]
  },
  {
    _id: 'Hachita',
    hobbies: [
      'theatre',
      'running',
      'poney',
      'reading',
      'computer science',
      'gaming'
    ]
  },
  {
    _id: 'Crawfordsville',
    hobbies: [
      'swimming', 'kung-fu',
      'poney',    'running',
      'cooking',  'theatre',
      'cinema',   'jardinage',
      'music',    'reading'
    ]
  },
  {
    _id: 'Warsaw',
    hobbies: [
      'running',   'reading',
      'swimming',  'poney',
      'jardinage', 'cinema',
      'gaming',    'music',
      'cooking',   'theatre'
    ]
  },
  {
    _id: 'Needmore',
    hobbies: [
      'computer science',
      'swimming',
      'jardinage',
      'cooking',
      'gaming',
      'theatre',
      'cinema',
      'running',
      'poney',
      'kung-fu'
    ]
  },
  {
    _id: 'Hayes',
    hobbies: [
      'kung-fu',
      'poney',
      'computer science',
      'gaming',
      'jardinage',
      'cooking',
      'music',
      'reading',
      'swimming'
    ]
  },
  {
    _id: 'Yettem',
    hobbies: [
      'cinema',
      'cooking',
      'gaming',
      'theatre',
      'swimming',
      'kung-fu',
      'computer science',
      'running',
      'music'
    ]
  }
]
Type "it" for more
```

18. Utiliser les projections ($project) pour lister les utilisateurs en n’aﬃchant que leur nom (en minuscule) et
    leur age.

```mongosh
db.users.aggregate([
  {$project: {name: {$toLower: "$name"}, age: 1}}
])
```

```console
[
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8c8'),
    age: 59,
    name: 'lynette mercer'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8c9'),
    age: 23,
    name: 'phillips blake'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8ca'),
    age: 48,
    name: 'casey gill'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8cb'),
    age: 43,
    name: 'frost franks'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8cc'),
    age: 12,
    name: 'cara young'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8cd'),
    age: 58,
    name: 'kramer humphrey'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8ce'),
    age: 54,
    name: 'armstrong ayers'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8cf'),
    age: 33,
    name: 'cameron cline'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d0'),
    age: 46,
    name: 'georgina rivas'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d1'),
    age: 57,
    name: 'wheeler boyer'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d2'),
    age: 55,
    name: 'britt huber'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d3'),
    age: 24,
    name: 'vanessa salas'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d4'),
    age: 15,
    name: 'forbes chang'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d5'),
    age: 24,
    name: 'jannie frazier'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d6'),
    age: 22,
    name: 'peggy snider'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d7'),
    age: 49,
    name: 'tameka carroll'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d8'),
    age: 48,
    name: 'petra thomas'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8d9'),
    age: 53,
    name: 'rivera lindsey'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8da'),
    age: 56,
    name: 'marie hansen'
  },
  {
    _id: ObjectId('668cadbe1eb707c3dba6e8db'),
    age: 25,
    name: 'maribel burns'
  }
]
Type "it" for more
```

19. Je souhaite savoir l’âge moyen des hommes de chaque état.

```mongosh
db.users.aggregate([
  {$match: {gender: "male"}},
  {$group: {_id: "$address.state", avgAge: {$avg: "$age"}}}
])
```

```console
[
  { _id: 'Rhode Island', avgAge: 33.85507246376812 },
  { _id: 'Oklahoma', avgAge: 32.82051282051282 },
  { _id: 'Iowa', avgAge: 35.1 },
  { _id: 'Michigan', avgAge: 31.52 },
  { _id: 'Maryland', avgAge: 36.426829268292686 },
  { _id: 'Nebraska', avgAge: 33.54794520547945 },
  { _id: 'West Virginia', avgAge: 34.940298507462686 },
  { _id: 'Idaho', avgAge: 33.916666666666664 },
  { _id: 'Illinois', avgAge: 35.71641791044776 },
  { _id: 'Pennsylvania', avgAge: 36 },
  { _id: 'Massachusetts', avgAge: 35.278688524590166 },
  { _id: 'Montana', avgAge: 33.57746478873239 },
  { _id: 'Alaska', avgAge: 35.298507462686565 },
  { _id: 'Kansas', avgAge: 32.42424242424242 },
  { _id: 'California', avgAge: 34.785714285714285 },
  { _id: 'Indiana', avgAge: 36.9746835443038 },
  { _id: 'Nevada', avgAge: 37.58730158730159 },
  { _id: 'South Dakota', avgAge: 33.343283582089555 },
  { _id: 'Oregon', avgAge: 34.111111111111114 },
  { _id: 'Arkansas', avgAge: 37.92307692307692 }
]
Type "it" for more
```
