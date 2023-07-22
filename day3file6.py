#Database programming using MongoDB

from pymongo import MongoClient

#Establishing mongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
print(type(conn_obj))

#creating objects
db_obj = conn_obj['Adv_PythonProgramming']  #DB object navigates database
col_obj = db_obj['Student']             # collection object navigates specific collection

#Fetching the first document
print('Find One Document:')
doc = col_obj.find_one()        #find_one() -> get first document
print(doc)

print('Find All Documents:')
#Fetching all the documents
# docs = col_obj.find()           #find() -> get list of all documents
# for doc in docs:
#     print(doc)

print("Finding document based on conditions")
#fetching based on conditions
# docs = col_obj.find({'Sex':'F'})
# for doc in docs:
#     print(doc)

# $gt - greater than, $lt - less than, $et - equal to, $ne - not equal to, $gte, $lte
# docs = col_obj.find({'Age':{'$lt':21}})
# for doc in docs:
#     print(doc)

print("Finding document with projection or filtered columns")
#Projection or filtering columns
# docs = col_obj.find({},{'Name':1,'Age':1,'Marks':1, '_id':0})
# for doc in docs:
#     print(doc)

print("sorted and limit applied document list")
#Sorting and liminting results
# docs = col_obj.find({}).sort("Age",1)
# for doc in docs:
#     print(doc)

# docs = col_obj.find({}).sort("Age",1).limit(2)
# for doc in docs:
#     print(doc)