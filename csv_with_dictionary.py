import csv
users = [{"name":"Pavan","phone":"7232323232","department":"testing"},
        {"name":"Vani","phone":"79192092","department":"Development"},
        {"name":"Munidhaar","phone":"723232","department":"Prod"},
        {"name":"Devansh","phone":"93324232","department":"Prod"}]

keys = ["name","phone","department"]

with open("dictionary_csv.csv","w") as dict:
    writer = csv.DictWriter(dict,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)