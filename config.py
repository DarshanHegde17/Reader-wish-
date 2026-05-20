from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["reader_wish"]

users_collection = db["users"]
books_collection = db["books"]
orders_collection = db["orders"]
cart_collection = db["cart"]
wishlist_collection = db["wishlist"]
feedback_collection = db["feedback"]
general_feedback_collection = db["general_feedback"]