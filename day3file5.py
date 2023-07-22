#Database programming using MongoDB

from pymongo import MongoClient

#Establishing mongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
print(type(conn_obj))

# Database- Adv_PythonProgramming and Collection - Student is already created in MongoDB compass
#Fetches the list of databases
db_list = conn_obj.list_database_names()
print("List of databases - ", db_list)

#Fetches the list of collections
db_obj = conn_obj['Adv_PythonProgramming']  #DB object navigates database
col_list = db_obj.list_collection_names()
print("List of collections - ",col_list)

#Inserting documents in collection - Student
col_obj = db_obj['Student']             # collection object navigates specific collection
document = {"Name": "Tanveer", "Age":24, "Subject": "Python", "Marks": 12.5}
return_val = col_obj.insert_one(document)
print(return_val)

document_list = [
    {'Name':'Kelley','Regd_id':'2','Age':21,'Sex':'M','Marks':12.5},
    {'Name':'Hannah','Regd_id':'3','Age':18,'Sex':'F'},
    {'Name':'Ravi','Regd_id':'4','Age':22,'Sex':'M'},
    {'Name':'Rachel','Regd_id':'5','Age':26,'Sex':'F'},
    {'Name':'Esther','Regd_id':'6','Age':19,'Sex':'F'}
]
return_val = col_obj.insert_many(document_list)
print(return_val)
