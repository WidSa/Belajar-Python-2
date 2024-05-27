# For Loop (Perulangan)

"""
for kondisi:
    aksi
"""
#  for dengan list
list_angka = [2, 4, 6, 8, 10]
print(list_angka)

for i in list_angka:
    print(f"perulangan i: {i}")

print("Akhir dari program 1"  + "\n")

#  for dengan range
list_angka2 = range(5)

for i in list_angka2:
    print(f"perulangan i: {i}")

print("Akhir dari program 2" + "\n")

list_angka2 = range(1,5)

for i in list_angka2:
    print(f"perulangan i: {i}")

print("Akhir dari program 3" + "\n")

# menggunakan string
data_string = "Andi"

for huruf in data_string:
    print(huruf)

print("Akhir dari program 4" + "\n")
