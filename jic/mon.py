
# def insert_document(col, document):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[col]

#     # Insert document into the collection
#     try:
#         collection.insert_one(document)
#         client.close()
#         return "inserted"
#     except Exception as e:
#         print(e)
#         client.close()
#         return "not inserted"
    
# def insert_document_opendb(client, db, col, document):

#     collection = db[col]

#     # Insert document into the collection
#     try:
#         collection.insert_one(document)
#         return 1
#     except Exception as e:
#         print(e)
#         return 0

# def update_document(document):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_responses]

#     # Insert document into the collection
#     try:
#         collection.update_one(document)
#         client.close()
#         return "updated"
#     except Exception as e:
#         print(e)
#         client.close()
#         return "no update"
    
# def update_many_documents(filter, set):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_responses]
#     try:
#         collection.update_many(filter, set)
#         client.close()
#         return "updated"
#     except Exception as e:
#         print(e)
#         return "no update"

# def upsert_document(collection_name, filter, new_document):
#     """
#     Perform an upsert operation on a MongoDB collection.
    
#     :param collection: The MongoDB collection where the upsert will be performed.
#     :param filter: A filter to identify the document to update or insert.
#     :param new_document: The document to replace the existing one or insert as a new document.
#     :return: The result of the upsert operation.
#     """
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_name]

#     result = collection.update_one(filter, {'$set': new_document}, upsert=True)
#     return result
    
# def check_existing(submission_year, target_pincode):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_responses]
    
#     # Create a query to find documents with the specified pincode
#     query = {"pincode": target_pincode, "submission_year": submission_year}
    
#     # Use the `find` method to search for documents that match the query
#     result = collection.find(query)
#     results = remove_id_field(result)
#     return len(results) > 0

# def search_documents_by_pincode(target_pincode):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_responses]

#     # Create a query to find documents with the specified pincode and year
#     query_ideal = {"pincode": target_pincode, "submission_year": 2024}
#     query_fallback = {"pincode": target_pincode, "submission_year": 2022}

#     # look for 2023 data first
#     result = remove_id_field(collection.find(query_ideal))

#     # if none, look for 2022 data
#     if len(result) == 0:
#         result = remove_id_field(collection.find(query_fallback))
    
#     # Use the `find` method to search for documents that match the query
#     return result

# def get_all_records(year: int = 2022):
#     # Connect to MongoDB
#     client, db = init_db()
#     collection = db[collection_responses]
    
#     # Create a query to find documents with the specified pincode
#     query = {"submission_year": year}
    
#     # Use the `find` method to search for documents that match the query
#     result = collection.find(query)
    
#     # Iterate over the results and print the matching documents
#     results = remove_id_field(result)

#     print(f"Found {len(results)} records")
#     return results