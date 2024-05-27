# Looping dari List

# For Loop
list_data = [8, 4, 10, 2, 6]

Peserta = ["Andi", "Budi", "Vaeli", "Dealy", "Lily"]
print("For Loop")
for nama in Peserta:
    print(f"nama: {nama}")

# for loop dan range
length = len(list_data)
print("\nFor Loop Ranga")
for i in range(length):
    print(f"Angka: {i}")

# While Loop
print("\nWhile Loop")
i = 0
while i < length:
    print(f"angka: {list_data[i]}")
    i+=1

# List Comprehension
print("\nList Comprehension")
data = ["Cecil", 7, 3, 10, "Maely"]
[print(f"Data: {i}") for i in data]

list_data = [8, 4, 10, 2, 6]
angka_kuadrat = [i**2 for i in list_data]
print(f"Angka sebelum: {list_data}, \nAngka sesudah: {angka_kuadrat}")

# Enumerate
print("\nEnumerate")
data = ["Cecil", 7, 3, 10, "Maely"]

for index,data in enumerate(data):
    print(f"index: {index}, Data: {data}")