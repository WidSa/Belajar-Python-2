# Looping Dictionary

Database =  {
    "Mahasiswa1" : "Celia",
    "Mahasiswa2" : "Beni",
    "Mahasiswa3" : "Zenya" 
}

#  Looping
for data in Database:
    print(data)

# Operator untuk mengambil items/ iterasi

# keys = Database.keys()
# print(keys)

for key in Database.keys():
    print(Database.get(key))

# values = Database.values()
# print(values)

for value in Database.values():
    print(value)

# items = Database.items()
# print(items)

for item in Database.items():
    print(item)

for key,value in Database.items():
    print(f"Kay: {key}, Value: {value}")

