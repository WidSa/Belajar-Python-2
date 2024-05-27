# Nested List 

# data_list = [[2, 6, 8], [3, 9, 7], [1, 4, 5]]
# print(data_list)

mahasisawa_1 = ["Andi", 1782684, "Manajamen", "Laki-laki"]
mahasisawa_2 = ["Sheila", 153736, "Akuntansi", "Perempuan"]
mahasisawa_3 = ["Veila", 1975455, "Sistem informasi" ,"Perempuan"]

list_mahasiswa = [mahasisawa_1, mahasisawa_2, mahasisawa_3]
# print(f"Peserta: {list_mahasiswa}\n")

# for mahasiswa in list_mahasiswa:
#     print(f"Nama\t: {mahasiswa[0]}")
#     print(f"NIM\t: {mahasiswa[1]}")
#     print(f"Jurusan\t: {mahasiswa[2]}")
#     print(f"Gender\t: {mahasiswa[3]}\n")

# dengan reference
list_copy = list_mahasiswa.copy()
mahasisawa_1[0] = "Bayu"
print(f"Mahaiswa: {list_copy}\n")
print(f"Peserta: {list_mahasiswa}\n")

