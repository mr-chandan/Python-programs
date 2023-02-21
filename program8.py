# write a program to demonstrate constructor and destructor

class MyClass:

    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


obj = MyClass()

# The object will be destroyed automatically when it goes out of scope
