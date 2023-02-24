# write a program to demonstrate at least six strings operations including split,search,join,modify



string = "Hello, world!"

words = string.split()
print("Splitting the string into words:", words)

substring = "world"
if substring in string:
    print("Substring found in the string.")

joined_string = " ".join(words)
print("Joining the list of words into a string:", joined_string)

new_string = string.replace("world", "Python")
print("Modifying the string by replacing a substring:", new_string)

uppercase_string = string.upper()
print("Converting the string to uppercase:", uppercase_string)

stripped_string = string.strip()
print("Removing whitespace from the string:", stripped_string)

print(string.find("world"))
