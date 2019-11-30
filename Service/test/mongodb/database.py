import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["garnachadbtest"]
#print(mydb)
mycol=mydb["UserVendedor"]


usuario1 = {"name":"Juan Perez", "correo":"juan99@hotmail.com","phone":"554239012"}
usuario2 = {"_id":4,"name":"Luis", "correo":"juan99@hotmail.com","phone":"554239012"}
usuario3 = {"_id":5,"name":"Pedro", "correo":"juan99@hotmail.com","phone":"554239012"}

listaUsuarios=[usuario1,usuario2,usuario3]
#x=mycol.insert_one(usuario)

#x=mycol.insert_many(listaUsuarios)

collist = mydb.list_collection_names()
if "UserVendedor" in collist:
     print("La coleccion existe")

busqueda={"name":"Pedro"}

mydoc=mycol.find(busqueda)

for x in mydoc:
     print(x)

#print(x.inserted_ids)
