import csv
f = open("file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone = row
    print("Name: {} , Phone:{}".format(name,phone))
f.close()