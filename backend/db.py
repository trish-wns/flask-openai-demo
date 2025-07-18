from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["myapp"]
users_collection = db["users"]
