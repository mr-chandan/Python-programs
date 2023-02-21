# write a program to perform following operations : create a cvs file ,insert values,operate on multiple columns,update and delete values

import csv

# Create a new CSV file and write header row
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Gender', 'Occupation'])

# Insert values into CSV file
with open('example.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['John Doe', '32', 'Male', 'Software Engineer'])
    writer.writerow(['Jane Smith', '27', 'Female', 'Data Analyst'])
    writer.writerow(['Bob Johnson', '45', 'Male', 'Sales Manager'])

# Read values from CSV file and perform operations
with open('example.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Operate on multiple columns
        if int(row['Age']) > 30:
            print(f"{row['Name']} is over 30 years old.")

        # Update value
        if row['Name'] == 'Bob Johnson':
            row['Occupation'] = 'Marketing Manager'
            print(
                f"{row['Name']}'s occupation has been updated to {row['Occupation']}.")

# Delete value
with open('example.csv', 'r') as csvfile:
    rows = []
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] != 'Jane Smith':
            rows.append(row)
    with open('example.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
