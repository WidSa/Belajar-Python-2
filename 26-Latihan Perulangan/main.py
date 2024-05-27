# Latihan Perulangan membuat segitiga

# input_sisi = int(input("Masukkan tinggi segitiga?: "))

sisi =  9

# Menggunakan for loop
# dummy variable
# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# menggunakan while
# count = 1
# while True:
#     print("*"*count)
#     count += 1
#     if count > sisi:
#         break

#  hanya ganjil
# count = 1
# while True:
#     # Akan kembali ke atas bila genap
#     if count % 2 == 0:
#         count += 1
#         continue
#     # akan print jika ganjil
#     print("*"*count)
#     count += 1
#     # akan break  jika count melebihi sisi
#     if count > sisi:
#         break

# segitiga sama kaki
count = 1
spasi = int(sisi/2)
while True:
    # Akan kembali ke atas bila genap
    if count % 2 == 0:
        count += 1
        continue
    # akan print jika ganjil
    else:
        print(" "*spasi,"*"*count)
        spasi -= 1
    count += 1
    # akan break  jika count melebihi sisi
    if count > sisi:
        break

count = (sisi-1)
spasi += 1

while True:
    if count % 2 == 0:
        count -= 1
        continue
    else:
        spasi += 1
        print(" "*spasi,"*"*count)
    count -= 1
    if count < 1:
        break

