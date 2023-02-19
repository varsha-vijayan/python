import csv
filename="data.csv"
columns=["Name","City"]
with open(filename,'r')as file:
    reader=csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
      for column in columns:
          column_without_space = column.strip()
          print(f"{column}:{row[column_without_space]}")
data.csv
Name,Age,City,Occupation
Arya,20,Bangloore,Developer
Megha,21,London,Designer
Anju,22,Paris,Manager
