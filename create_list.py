import csv

csv_file = open("test_list.csv")
data = str(list(csv.reader(csv_file, delimiter=",")))

with open("test_list.py", "w") as file:
    file.write(data)
