# Copy dictionary

database = {
    "peserta_1" : "Sandy",
    "peserta_2" : "Ellen",
    "peserta_3" : "Cecil"
}

member = database.copy()

print(f"Database: {database}\n")
print(f"Member: {member}\n")

database["peserta_2"] = "Andy"

print(f"Database: {database}\n")
print(f"Member: {member}\n")

# pop dictionary
data_group = member.pop("peserta_2")

print(f"Data Group: {data_group}\n")
print(f"Member: {member}\n")

# pop item dictionary
data_terakhir = database.popitem()
print(f"Data Terakhir: {data_terakhir}\n")
print(f"Member: {database}\n")

