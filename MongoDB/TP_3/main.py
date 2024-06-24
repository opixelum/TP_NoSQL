from pymongo import MongoClient

# MONGOD_URI = "mongodb://root:example@localhost"
MONGODB_URI = "mongodb+srv://rakibhernandez:VfSPj19EebJUFGTn@cluster0.cqmhdye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

if __name__ == "__main__":
    client = MongoClient(MONGODB_URI)

    for db_name in client.list_database_names():
        print(db_name)

    client.get_database("sample_mflix")
    
    client.close()