import sys
from tabulate import tabulate
import csv


if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
     with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            table = tabulate(reader, headers="keys", tablefmt="grid")
            print(table)

        # print(reader.fieldnames)
except (FileNotFoundError):
    sys.exit("File not found!")