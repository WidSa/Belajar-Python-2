import datetime as dt
import os
import string
import random

# Tamplate dict mahasiswa
template_mahasiswa = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks' : 0,
    'lahir' : dt.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("clear")
    print(f"{'Selamat Datang':^15}")
    print(f"{'Data Mahasiswa':^15}")
    print("="*35)

    mahasiswa = dict.fromkeys(template_mahasiswa.keys())

    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks'] = int(input("SKS Mahasiswa: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<10} {'NIM':<9} {'SKS':^7} {'Lahir':^10}")
    print("="*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<10} {NIM:<9} {SKS:^7} {LAHIR:^10}")

    print("\n")
    is_done = input("Apakah sudah selesai input (Y/N)? ")

    if is_done == 'Y' or is_done == 'y':
        break 

print("Akhir Dari Program")
