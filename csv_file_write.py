import csv
hosts=[["workstation.local","198.12.24.2"],["workstation.cloud","23.234.32"]]
with open("file1.csv","w") as csv_f:
    writer = csv.writer(csv_f)
    writer.writerows(hosts)