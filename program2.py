# write a program to display the sum of all the even numbers between a user inputted range. Implement using for and while loop


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))


sum_of_evens_for = 0
sum_of_evens_while = 0
num = start


for num_for in range(start, end+1):
    if num_for % 2 == 0:
        sum_of_evens_for += num_for


while num <= end:
    if num % 2 == 0:
        sum_of_evens_while += num
    num += 1


print("The sum of even numbers between", start, "and", end, "using for loop is", sum_of_evens_for)
print("The sum of even numbers between", start, "and", end, "using while loop is", sum_of_evens_while)


