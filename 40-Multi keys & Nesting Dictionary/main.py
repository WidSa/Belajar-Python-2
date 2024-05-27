import datetime

mahasiswa1 = {
    'nama' : 'Cecil',
    'nim' : '186743846',
    'sks' : 132,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2001,8,21)
}
mahasiswa2 = {
    'nama' : 'Brian',
    'nim' : '15835197',
    'sks' : 127,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2002,8,21)
}
mahasiswa3 = {
    'nama' : 'Vanie',
    'nim' : '19635444',
    'sks' : 116,
    'beasiswa' : True,
    'lahir' : datetime.datetime(1999,8,21)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

print("="*40)
print(f"{'KEY':<6} {'NAMA':<10} {'SKS':<4} {'Beasiswa':<7} {'Lahir':<10}")
print("="*40)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<10} {SKS:<7} {BEASISWA:<6} {LAHIR:<8}")
    

