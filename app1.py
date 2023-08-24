# write a script to connect with mongodb and read the data first

from pymongo import MongoClient
try:
    client=MongoClient('127.0.0.1',27017)
    print('MongoDB Server Connected')
    db=client['loverboy']
    collection=db['cse']

    for i in collection.find():
        print(i)
except:
    print('MongoDB Server Failed')