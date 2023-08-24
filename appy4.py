from pymongo import MongoClient
try:
    Client=MongoClient('127.0.0.1',27017)
    print("MONGO db server connected")
    db=Client['loverboy']
    collection=db['cse']
    query={'name':'roll'}
    for i in collection.find(query):
        print(i)
except:
    print("server not connected")