# Operasi pada List

numbers = [9, 7, 8, 6, 8, 7, 8, 6, 9, 9]
print(f"Data: {numbers}")

# Count data

jumlah_data_9 = numbers.count(9)
jumlah_data_8 = numbers.count(8)

print(f"Jumlah angka 9: {jumlah_data_9}")
print(f"Jumlah angka 8: {jumlah_data_8}")

#  Ambil posisi data

data = ["andi", "cecil", "sheila", "budi", "leila"]
print(f"data: {data}")

index_sheila = data.index("sheila")
print(f"Index sheila: {index_sheila}")

# mengurutkan list
print(f"Data Numbers sebelum sort: \n{numbers}")
numbers.sort()
print(f"Data Numbers Sort: \n{numbers}")

print(f"Data Nama sebelum sort: \n{data}")
data.sort()
print(f"Data Numbers Sort: \n{data}")

# reverse pengurutan list
print(f"Data Numbers sebelum Reverse: \n{numbers}")
numbers.reverse()
print(f"Data Numbers Reverse: \n{numbers}")

