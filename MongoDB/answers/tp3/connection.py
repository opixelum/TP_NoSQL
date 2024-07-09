from datetime import datetime, timezone
from bson.objectid import ObjectId
from pymongo import MongoClient


# Anto Benedetti 3IABD2


MONGODB_URI = "mongodb://root:example@localhost"
MONGODB_URI_ONLINE = "mongodb+srv://user1:aUTP20Mn6iFg9v8F@esgi.a3qbntn.mongodb.net/?retryWrites=true&w=majority&appName=ESGI"


def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=0.0
):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount}
    }

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    # Opération 3 : Ajouter un nouveau transfer vers la collection transfers
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")
    return


def callback_wrapper1(session):
    callback(
        session,
        transfer_id="TR723256981",
        account_id_receiver="MDB333829449",
        account_id_sender="MDB955769550",
        transfer_amount=20.93
    )


def callback_wrapper2(session):
    callback(
        session,
        transfer_id="TR484655391",
        account_id_receiver="MDB672307611",
        account_id_sender="MDB829751145",
        transfer_amount=12.45
    )


if __name__ == "__main__":
    client = MongoClient(MONGODB_URI)
    databases = client.list_database_names()
    print(databases)
    # Output
    # ['admin', 'config', 'geospatial', 'local', 'test', 'test_compass', 'weather-data']
    client.close()

    client = MongoClient(MONGODB_URI_ONLINE)
    databases = client.list_database_names()
    print(databases)
    # Output
    # ['sample_mflix', 'admin', 'local']
    client.close()

    # Insert
    client = MongoClient(MONGODB_URI)
    db = client.bank
    account_collection = db.accounts

    # insert_one
    new_account = {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB829001337",
        "account_type": "checking",
        "balance": 50352434,
        "last_updated": datetime.now(tz=timezone.utc),
    }
    result = account_collection.insert_one(new_account)
    inserted_id = result.inserted_id
    print("_id of inserted document: {inserted_id}")

    # insert_many
    new_accounts = [
        {
            "account_id": "MDB011235813",
            "account_holder": "Ada Lovelace",
            "account_type": "checking",
            "balance": 60218,
        },
        {
            "account_id": "MDB829000001",
            "account_holder": "Muhammad ibn Musa al-Khwarizmi",
            "account_type": "savings",
            "balance": 267914296,
        }
    ]
    result = account_collection.insert_many(new_accounts)
    inserted_id = result.inserted_ids
    print("# of documents inserted: " + str(len(inserted_id)))
    print("_id of inserted document: {inserted_ids}")

    # Find
    db = client.sample_training
    zips_collection = db.zips

    # 1. Récupérez l’ensemble des états avec la valeur AZ.
    az_entries = list(zips_collection.find({"state": "AZ"}))
    for entry in az_entries:
        print(entry)

    # 2. Renvoyez le nombre de zips dont la ville est soit dans PHOENIX soit dans CHICAGO.
    cities_count = zips_collection.count_documents({"city": {"$in": ["PHOENIX", "CHICAGO"]}})
    print("Number of zips in PHOENIX or CHICAGO:", cities_count)

    # 3. Changeons de Dataset, maintenant nous souhaitons récupérer cette information
    # depuis la base de donnée sample_supplies/sales { _id: ObjectId("5bd761dcae323e45a93ccff4")}
    db = client.sample_supplies
    sales_collection = db.sales
    sales_entry = sales_collection.find_one({"_id": ObjectId("5bd761dcae323e45a93ccff4")})
    print(sales_entry)

    # 4. Et enfin, nous souhaitons récupérer l’ensemble de la base de donnée storeLocation
    # qui est à la fois à New York mais aussi à London { storeLocation: { $in: ["London", "New York"] } }
    store_locations = list(sales_collection.find({"storeLocation": {"$in": ["London", "New York"]}}))
    for location in store_locations:
        print(location)

    # Opérateurs
    # 1. Trouver les ventes comprenant un article dont le prix est supérieur à 200$
    sales_above_200 = list(sales_collection.find({"items.price": {"$gt": 200}}))
    for sale in sales_above_200:
        print(sale)

    # 2. Trouvez tous les documents qui contiennent un article dont le prix est inférieur à 25$.
    sales_below_25 = list(sales_collection.find({"items.price": {"$lt": 25}}))
    for sale in sales_below_25:
        print(sale)

    # 3. Recherchez tous les documents contenant un article dont la quantité est supérieure ou égale à 10.
    sales_quantity_10_or_more = list(sales_collection.find({"items.quantity": {"$gte": 10}}))
    for sale in sales_quantity_10_or_more:
        print(sale)

    # 4. Recherchez tous les documents concernant une vente à un client âgé de 45 ans ou moins.
    sales_customer_45_or_less = list(sales_collection.find({"customer.age": {"$lte": 45}}))
    for sale in sales_customer_45_or_less:
        print(sale)

    # Bank account
    db = client.bank
    accounts_collection = db.accounts

    # 1. Ecrire un programme en python qui va chercher l’object id de
    # 62d6e04ecab6d8e1304974ae dans bank.accounts
    document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}
    account = accounts_collection.find_one(document_to_find)
    if account:
        print(account)
    else:
        print("No document found with the specified ObjectId")

    # 2. Ecrire un programme en python qui va chercher tout les comptes en
    # banque dont la somme est supérieur à 4700$
    documents_to_find = {"balance": {"$gt": 4700}}
    accounts = accounts_collection.find(documents_to_find)
    if accounts:
        for account in accounts:
            print(account)
    else:
        print("No accounts found with a balance greater than 4700$")

    # Update
    # 1. Ecrire un programme en python qui va ajouter 200$ à tout les comptes en banques.
    select_all_accounts = {}
    add_200_to_all_accounts = {"$inc": {"balance": 200}}
    result = accounts_collection.update_many(select_all_accounts, add_200_to_all_accounts)
    print(f"Nombre de documents mis à jour: {result.modified_count}")

    # 2. Ecrire un code répondant permettant d’ajouter 50$ à tout le monde avec
    # le numéro de transaction donnée dans la consigne.
    select_accounts = {"account_type": "checking"}
    add_transfer = {
        "$inc": {"balance": 50},
        "$push": {"transfers_complete": "TR413308000"}
    }
    result = accounts_collection.update_many(select_accounts, add_transfer)
    print(f"Nombre de documents mis à jour: {result.modified_count}")

    # Delete
    # 1. Ecrivez un code permettant de supprimer un document ayant pour
    # identifiant unique ObjectId("62d6e04ecab6d8e130497485").
    document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}
    result = accounts_collection.delete_one(document_to_delete)
    if result.deleted_count > 0:
        print("Document deleted successfully.")
    else:
        print("No document found with the specified ObjectId.")

    # 2. Ecrivez un code permettant de supprimer un ensemble de document en
    # fonction d’un filtre suivant : Supprimer tout les comptes en banque dont
    # le balance est inférieur à 500.
    documents_to_delete = {"balance": {"$lt": 500}}
    result = accounts_collection.delete_many(documents_to_delete)
    print(f"Number of documents deleted: {result.deleted_count}")

    # Transaction
    with client.start_session() as session:
        session.with_transaction(callback_wrapper1)
        session.with_transaction(callback_wrapper2)

    client.close()
