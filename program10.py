# write a program to perform following operations : create a cvs file ,insert values,operate on multiple columns,update and delete values

import csv

# Create
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Gender', 'Occupation'])
    csvfile.close()

# Insert
with open('example.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Ram', '32', 'Male', 'Software Engineer'])
    writer.writerow(['bam', '27', 'Female', 'Data Analyst'])
    writer.writerow(['sham', '45', 'Male', 'Sales Manager'])
    csvfile.close()

# Read
with open('example.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
    csvfile.close()

# Delete
with open('example.csv', 'r') as csvfile:
    updaterow = []
    reader = csv.reader(csvfile)
    delname = input("Enter the name you want to delete : ")
    for row in reader:
        print(row)
        if row[0] != delname:
            updaterow.append(row)
    with open('example.csv', 'w', newline='') as csvfile:
        upd = csv.writer(csvfile)
        upd.writerows(updaterow)

# Update value
with open('example.csv', 'r') as csvfile:
    uprow = []
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] != 'bam':
            uprow.append(row)
        else:
            row[3] = 'Marketing Manager'
            uprow.append(row)
    with open('example.csv', 'w', newline='') as csvfile:
        upd = csv.writer(csvfile)
        upd.writerows(uprow)
