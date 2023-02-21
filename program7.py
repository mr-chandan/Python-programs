# write a program to demonstrate dictionary operations: items,values,update,copy,keys etc


my_dict = {"apple": 1, "banana": 2, "orange": 3}

keys = my_dict.keys()
print(keys)  # dict_keys(['apple', 'banana', 'orange'])

values = my_dict.values()
print(values)  # dict_values([1, 2, 3])

items = my_dict.items()
print(items)  # dict_items([('apple', 1), ('banana', 2), ('orange', 3)])

my_dict["grape"] = 4
print(my_dict)  # {'apple': 1, 'banana': 5, 'orange': 3, 'grape': 4}

my_dict_copy = my_dict.copy()
print(my_dict_copy)  # {'apple': 1, 'banana': 5, 'orange': 3, 'grape': 4}

my_dict.pop("orange")
print(my_dict)  # {'apple': 1, 'banana': 5, 'grape': 4}

my_dict.clear()
print(my_dict)  # {}
