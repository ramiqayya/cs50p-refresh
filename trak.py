import csv


with open("marawan.csv", "r") as file:
    mad=csv.DictReader(file)
    for row in mad:
        print(f'{row["Jesh ej"]} or {row[" takeha"]}')

    