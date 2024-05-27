# Teknik menduplikan list

numbers = [1, 3, 4, 5, 6]
print(f"Numbers: {numbers}")

data = numbers # => pass by reference
print(f"Data: {data}\n")

# merubah member list numbers
numbers[0] = 9
data.sort()

print(f"Numbers: {numbers}")
print(f"Data: {data}\n")

# Addres data numbers
print(f"Address Numbers: {hex(id(numbers))}")
print(f"Address Data: {hex(id(data))} \n")

# menduplikat list dengan copy
list_angka = numbers.copy() # => full duplicate/ data baru

print(f"Address Numbers: {hex(id(numbers))}")
print(f"Address Data: {hex(id(data))}")
print(f"Address List angka: {hex(id(list_angka))} \n")
list_angka[1] = 7

list_angka.reverse()
print(f"Numbers: {numbers}")
print(f"Data: {data}")
print(f"List angka: {list_angka}\n")

