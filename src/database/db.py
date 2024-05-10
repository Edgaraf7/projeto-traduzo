import os
from pymongo import MongoClient

# Verifica se a variável de ambiente MONGO_URI está definida
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Verifica se a variável de ambiente DB_NAME está definida
db_name = os.getenv("DB_NAME", "test_db_traduzo")

# Conexão com o MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]

# Definição das coleções (collections)
languages_collection = db["languages"]
users_collection = db["users"]
translations_collection = db["translations"]
