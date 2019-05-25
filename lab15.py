import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["lab15"]
mycol = mydb["producto"]

print(mydb.)
mylist = [
    {"item":"lapiz","marca":"bolik","numero":2,"precio": 2},
    {"item":"carro","marca":"toyota","kilometraje":5000,"gasolina":"super","precio":120000},
    {"item":"pachon","volumen":1.5,"color":"rojo","precio":50},
    {"item":"laptop","marca":"sager","RAM":16,"procesador":"i7-7800","pantalla":15.3,"precio":8000},
    {"item":"mousepad","color":"negro","precio":25}
    ]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
