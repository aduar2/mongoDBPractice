import pymongo
import os
import sys
import pprint

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test'] #1. put the name of your collection in the quotes
    
    doc = {"title": "The Bell Jar", "author": "Slyvia Plath", "copyright": 1971}
    collection = collection.insert_one(doc) #2. add a document to your collection using the insert_one method
    doc = {"title": "Skin", "author": "Roald Dahl", "copyright": 2000}
	collection = collection.insert_one(doc)
	doc = {"title": "The Missing Piece", "author": "Shel Silverstein", "copyright": 1976}
	collection = collectioninsert_one(doc)    
    
    
    collection.count_documents({})#3. print the number of documents in the collection
    
    #4. print the first document in the collection
    pprint.pprint collection.find()
    
    #5. print all documents in the collection
    for doc in collection.find():
    	print(doc)
    
    #6. print all documents with a particular value for some attribute
    collection.find_one({"author": "Shel Silverstein"})
    #ex. print all documents with the birth date 12/1/1990
    
    
if __name__=="__main__":
    main()