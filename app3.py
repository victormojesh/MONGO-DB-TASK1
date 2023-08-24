# write a script to connect with mongodb and read the data first

from pymongo import MongoClient
try:
    client=MongoClient('127.0.0.1',27017)
    print('MongoDB Server Connected')
    db=client['loverboy']
    collection=db['cse']
    name=input('enter name:')
    rollno=input('enter roll no:')
    k={}
    k['name']=name
    k['rollno']=rollno
    collection.insert_one(k) #will be doing insertion


    for i in collection.find():
        pass
    else:
        print(i)
except:
    print('Mongodb server failed')
  
