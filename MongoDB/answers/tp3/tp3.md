# TP 3

Anto Benedetti 3IABD2

1. Quelle est la principale responsabilité d’un pilote MongoDB ?

B. Établir des connexions sécurisées avec un cluster MongoDB et exécuter des opérations de base de données pour le compte d’applications clientes.

2. Quel est le driver que nous utiliserons pour les applications synchrone de python ?

B. PyMongo

## CRUD

Les commandes mongosh sont ici.
Pour la partie python, voir le fichier python.

1. insertOne

```mongosh
db.accounts.insertOne({
  "account_id": 111333,
  "limit": 12000,
  "products": [
  "Commodity",
  "Brokerage"
  ],
  "last_updated": new Date()
})
```

```console
{
  acknowledged: true,
  insertedId: ObjectId('668d693648b52a966f149f48')
}
```

2. insertMany

```mongosh
db.accounts.insertMany([
  {
    "account_id": 111333,
    "limit": 12000,
    "products": [ "Commodity", "Brokerage"],
    "last_updated": new Date()
  },
  {
    "account_id": 678943,
    "limit": 8000,
    "products": [ "CurrencyService", "Brokerage", "InvestmentStock"],
    "last_updated": new Date()
  },
  {
    "account_id": 321654,
    "limit": 10000,
    "products": [ "Commodity", "CurrencyService"],
    "last_updated": new Date()
  }
])
```

```console
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('668d698048b52a966f149f49'),
    '1': ObjectId('668d698048b52a966f149f4a'),
    '2': ObjectId('668d698048b52a966f149f4b')
  }
}
```
