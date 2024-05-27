# Operasi

data = ["celia", "andi", "budi", "velia", "sheila"]

# mengambil list
data_0 = data[0]
print(f"Data Pertama (index-0): {data_0}")

data_terakhir = data[-1]
print(f"Data Terakhir : {data_terakhir}")

# mengambil info jumlah data dalam list
length_list = len(data)
print(f"Panjang Data: {length_list}")

# Memanipulasi Data List
## Menambah data 
print(f"Data sebelum add: \n{data}\n")

data.insert(1, "dwi")
print(f"Data setelah add: \n{data}\n")

# Menambah diakhir lis
data.append("ui")
print(f"Data ditambah diakhir: \n{data}\n")

# menggambungkan list
data_baru = ["koji", "weina", "bael"]
data.extend(data_baru)
print(f"Data gabungan: \n{data}\n")

# Merubah data dalam list
data[1] = "friena"
print(f"Data dirubah: \n{data}\n")

# Menghapus data dalam list =>case sensitif
data.remove("ui")
print(f"data dihapus: \n{data}\n")

# menghapus data akhir di dalam list
data.pop()
print(f"data akhir dihapus: \n{data}\n")

