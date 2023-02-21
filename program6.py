# write a program to demonstrate list operations: append,extend,insert,pop,slice,count etc

my_list = [1, 2, 3]

my_list.append(4)
print(my_list)  # output: [1, 2, 3, 4]

my_list.extend([5, 6])
print(my_list)  # output: [1, 2, 3, 4, 5, 6]

my_list.insert(2, 2.5)
print(my_list)  # output: [1, 2, 2.5, 3, 4, 5, 6]

removed = my_list.pop(2)
print(my_list)  # output: [1, 2, 3, 4, 5, 6]
print(removed)  # output: 2.5

slice = my_list[1:4]
print(slice)  # output: [2, 3, 4]

count = my_list.count(2)
print(count)  # output: 1

my_list.reverse()
print(my_list)  # output: [6, 5, 4, 3, 2, 1]

my_list.sort()
print(my_list)  # output: [1, 2, 3, 4, 5, 6]
