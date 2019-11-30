import pymongo

def dbconnect(dbName):
     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
     #myclient = pymongo.MongoClient(ip)
     mydb=myclient[dbName]
     return mydb

def showCols(db):
     colList=db.list_collection_names()
     return colList

def useCol(mydb,colName):
     mycol=mydb["UserVendedor"]
     return mycol

def insert2Col(col,data):
     x=col.insert_one(data)
     #x=mycol.insert_many(listaUsuarios)

def find(col,query):
     #busqueda={"name":"Pedro"}
     cons=col.find(query)
     return cons
