# write a program to demonstrate mutability and immutability of python strings,lists,and tuples

s = "hello"

try:
     s[0] = "H"
except:
    print("error occoured")     
    
    
l = [1, 2, 3]
try:
    l[0] = 4
except:
    print("error occoured") 
else:
    print("no error in list")


t = (1, 2, 3)
try:
     t[0] = 4
except:
    print("error occoured")    