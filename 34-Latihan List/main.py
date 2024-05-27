# Program List Buku

list_buku = []
while True:
    print("\nMasukkan Data Buku")
    judul = input("Judul buku\t: ")
    Penulis = input("Nama Penulis\t: ")

    buku_baru = [judul, Penulis]
    list_buku.append(buku_baru)

    print("\nData Buku")
    print("No.\t| Judul\t\t| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index}\t| {buku[0]}\t| {buku[1]}")
        print("="*35)

    print("\n\n")
    isLanjut = input("Apakah dilanjutkan?(y/n) ")
    if isLanjut == 'N' or isLanjut == 'n':
        break
    elif isLanjut == 'Y' or isLanjut == 'y':
        pass

print("Program Selesai")



