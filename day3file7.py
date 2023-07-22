#Database programming using MongoDB

from pymongo import MongoClient

#Establishing mongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
print(type(conn_obj))

#creating objects
db_obj = conn_obj['Adv_PythonProgramming']  #DB object navigates database
col_obj = db_obj['Student']             # collection object navigates specific collection

#Update one record
col_obj.update_one({'Regd_id':'3'},{'$set':{'Age':25}})
#Update many records
col_obj.update_many({'Regd_id':{'$gt':'4'}},{'$set':{'Age':24}})
docs = col_obj.find({},{'_id':0,'Regd_id':1,'Age':1})
for doc in docs:
    print(doc)

print("Deleting records")
#Delete one record
col_obj.delete_one({'Regd_id':'1'})
#Delete many records
col_obj.delete_many({'Regd_id':{'$gt':'4'}})
docs = col_obj.find({},{'_id':0,'Regd_id':1,'Age':1})
for doc in docs:
    print(doc)


#Dropping the collection
# col_obj.drop()
# print('After Dropping the collection:')
# for doc in col_obj.find():
#     print(doc)