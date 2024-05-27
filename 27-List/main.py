# List 

#  Kumpulan data numbers
numbers = [8, 7, 6, 9, 5]
print(numbers)

# kumpulan data string
data_String = ["andi", "sheila", "budi", "dodi", "celia"]
print(data_String)

# kumpulan data boolean
data_boolean = [True, False, False, True, True]
print(data_boolean)

# kumpulan data campuran
data_mix = [7, "Velia", False, "Beilla", True]
print(data_mix)

# cara alternatif list
data_range = range(1, 11, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# list dengan for loop
list_for = [i**2 for i in range(1,6)]
print(list_for)

# List dengan for dan if
list_for_if = [i for i in range(1,11) if i % 2 == 0]
print(list_for_if)