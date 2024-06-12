import pymongo
import bson

def restore_mongodb_dataset(uri, database_name, collection_name, input_file):
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)
    
    # Access the specified database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Read the BSON file and insert documents into the collection
    with open(input_file, 'rb') as f:
        while True:
            try:
                # Read the next document from the BSON file
                raw_doc = bson.decode_all(f.read())
                
                if not raw_doc:
                    break

                for doc in raw_doc:
                    # Insert the document into the collection
                    collection.insert_one(doc)

            except EOFError:
                break
    
    print(f"Data from {input_file} has been restored to {database_name}.{collection_name}")

if __name__ == "__main__":
    # MongoDB connection URI
    uri = "mongodb://root:example@localhost:27017/"

    
    # Database and collection to restore
    database_name = "bank"
    account_collection = "accounts"
    transfers_collection = "transfers"
    
    # Input file
    input_file_account = "accounts.bson"
    input_file_transers = "transfers.bson"
    
    restore_mongodb_dataset(uri, database_name, account_collection, input_file_account)
    restore_mongodb_dataset(uri, database_name, transfers_collection, input_file_transers)
