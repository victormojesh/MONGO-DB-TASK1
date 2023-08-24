# connect with mongoDB
from pymongo import MongoClient
try:
    client=MongoClient('127.0.0.1',27017)
    print('MongoDB Server Connected')
except:
    print('MongoDB Server Failed')