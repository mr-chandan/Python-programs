# write a program to demonstrate mutability and immutability of python strings,lists,and tuples


s = "hello"
# This line will raise a TypeError since strings are immutable
s[0] = "H"
print("String s = ", s)


l = [1, 2, 3]
print("List before mutation:", l)
# No error as lists are mutable
l[0] = 4
print("List l = ", l)


t = (1, 2, 3)
# This line will raise a TypeError since tuples are immutable
# t[0] = 4
print("Tuple t = ", t)
