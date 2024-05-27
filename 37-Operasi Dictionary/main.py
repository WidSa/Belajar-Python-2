#  Operator Dictionary

data_dict = {
    "nama_1" : "Sarah",
    "nama_2" : "Vanesa",
    "nama_3" : "Andi"
}

#  Panjang dictionary
lendict = len(data_dict)

print(f"Panjang dictionary: {lendict}")

#  mengecheck key ada atau tidak
key = "nama_1"
check_key = key in data_dict
print(f"Apakah {key} ada di data_dict: {check_key}")

#  mengakses value (read) dengan get

print(data_dict["nama_1"])
print(data_dict.get("nama_2"))
print(data_dict.get("nama_5", "key tidak ada")) # cek key dengan massage/none

#  mengupdate data
data_dict["nama_1"] = "Selly"
print(data_dict)

data_dict["nama_4"] = "Budi"
print(data_dict)

data_dict.update({"nama_4" : "Larry"})
print(data_dict)
data_dict.update({"nama_5" : "Xel"})
print(data_dict)

#  menghapus data pada dictionary
del data_dict["nama_4"]
print(f"\n {data_dict}")





