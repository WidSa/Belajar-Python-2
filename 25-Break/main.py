# Break

# angka = 0

# while angka < 5:
#     angka += 1
#     print(f"Angka : {angka}")
#     if angka == 3:
#         print("Cukup")
#         break
#     print("Lanjut")

# print("Akhir dari program")

angka = 5

while True:
    tebak_angka = int(input("Tebak angka dari 1-10?: "))
    if tebak_angka < angka:
        print("Angkanya lebih dari itu\n")
    elif tebak_angka > angka:
        print("Angkanya kurang dari itu\n")
    elif tebak_angka == angka:
        print(f"Selamat, {tebak_angka} adalah angka yang tepat")
        break


print("Akhir dari program")