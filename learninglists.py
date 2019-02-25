my_list = [1, 2, 3]
nested_list = []

nested_list.append(123)
nested_list.append(22)
nested_list.append('ntp')
nested_list.append('ssh')

print(my_list)
print(my_list[0])
print(my_list[1])

my_list.append("four")
print(my_list)

del my_list[2]
print(my_list)

my_list.append(nested_list)
print(my_list)

print(my_list[3])

print(my_list[3][2])

# print(my_list[0][1])

print(my_list[2][1])

sliced = my_list[1:3]
print(sliced)

slice_me = "ip address"
sliced = slice_me[:2]
print(sliced)
