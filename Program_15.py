# WAP that reads data from a CSV file and prints it to the console
import csv
f = open("student.csv",'r')
csv_reader = csv.reader(f)
for row in csv_reader:
    print(row)
f.close()