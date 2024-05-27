# Continue dan Pass

# Pass => berfungsi sebagai dummy tidak akan dieksekusi

angka = 1

# while angka <= 15:
#     if angka % 3 == 0 and angka % 5 == 0:
#         print("FuzzBuzz")
#     elif angka % 3 == 0:
#         print("Fuzz")
#     elif angka % 5 == 0:
#         print("Buzz")
#     else:
#         print(angka)
#     angka += 1


# while angka < 5:
#     print(angka)
#     if angka == 3:
#         pass
#     angka += 1

# print("Akhir dari program")

# Continue => akan membuat loop meloncat ke perulangan selanjutnnya
angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang : {angka}")
    if angka == 3:
        print("Nice")
        continue
    print("Oke")

print("Akhir dari program")