
data_0 = [2,4]
data_1 = [1,3]

data_2d = [data_0,data_1, 9]
data_2d_copy = data_2d.copy()

print(f"Data: {data_2d}")
print(f"Data Copy: {data_2d_copy}")

# Mengambil data dari nested list
data = data_2d[0][1]
print(f"data: {data}\n")

# address semua data
print(f"adress asli: {hex(id(data_2d))}")
print(f"adress Copy: {hex(id(data_2d_copy))}\n")

print("Address dari member ke-1")
print(f"adress asli: {hex(id(data_2d[0]))}")
print(f"adress Copy: {hex(id(data_2d_copy[0]))}\n")

data_2d[1][0] = 5
data_2d[2] = 8
print(f"Data: {data_2d}")
print(f"Data Copy: {data_2d_copy}\n")

# Deep Copy => gunakan deep copy jika nested list
from copy import deepcopy

data_2d_deepCopy = deepcopy(data_2d)

print(f"Data: {data_2d}")
print(f"Data DeepCopy: {data_2d_deepCopy}\n")

print("Address dari member ke-1")
print(f"adress asli: {hex(id(data_2d[0]))}")
print(f"adress DeepCopy: {hex(id(data_2d_deepCopy[0]))}\n")

data_2d[1][0] = 7
data_2d[2] = 10
print(f"Data: {data_2d}")
print(f"Data Copy: {data_2d_copy}")
print(f"Data DeepCopy: {data_2d_deepCopy}\n")

