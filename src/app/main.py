from app.core.mongo_connector import MongodbConnector
from app.models.brain_mapper import BrainMapper

import logging
from app import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main() -> None:
    logger.info("Application started")
    logger.info("Hello noobs")
    query = 'collection.find().sort("price", -1).limit(1)'
    sentence = "find item with max price"
    data = {sentence: query}
    BrainMapper(data)

def add_sample_data():
    con = MongodbConnector().client
    db = con["shop"]
    collection = db["order"]
    sample_data = [
        {"name": "Laptop", "price": 55000, "qty": 2, "category": "Electronics"},
        {"name": "Smartphone", "price": 30000, "qty": 5, "category": "Electronics"},
        {"name": "Desk Chair", "price": 7000, "qty": 3, "category": "Furniture"},
        {"name": "Pen", "price": 20, "qty": 50, "category": "Stationery"},
        {"name": "Notebook", "price": 50, "qty": 100, "category": "Stationery"},
        {"name": "Monitor", "price": 12000, "qty": 4, "category": "Electronics"},
        {"name": "Water Bottle", "price": 150, "qty": 20, "category": "Kitchen"},
        {"name": "Headphones", "price": 2500, "qty": 6, "category": "Electronics"}
    ]
    collection.insert_many(sample_data)

if __name__ == "__main__":
    main()