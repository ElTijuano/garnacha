from mongodb import *


def newUserClient(ClientId,nombre,token):
     userClient={
          "_id":ClientId,
          "name":nombre,
          "token":token
     }
     return userClient

def newUserSeller(SellerId,nombre,telefono,passwd,CLABE,banco):
     userSeller={
          "_id":SellerId,
          "name":nombre,
          "phone":telefono,
          "passwd":passwd,
          "CLABE":CLABE,
          "bank":banco
     }
     return userSeller


def newChangarro(ChangarroId,Nombre, SellerId, menu, location):
     changarro={
          "_id":ChangarroId,
          "name":Nombre,
          "sellerId":SellerId,
          "location":location,
          "manu":menu
     }
     return changarro

def addUserClient(db,userClient):
     col=useCol(db,"Clients")
     insert2Col(col,userClient)

def addUserSeller(db,userSeller):
     col=useCol(db,"Seller")
     insert2Col(col,userSeller)

def addChangarro(db,changarro):
     col=useCol(db,"Changarro")
     insert2Col(col,changarro)

