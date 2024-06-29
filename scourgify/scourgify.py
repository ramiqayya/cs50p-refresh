import csv
import sys

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
try:
    with open(sys.argv[1],"r") as before, open(sys.argv[2],"w") as after:
        reader=csv.DictReader(before)
        # print(reader.fieldnames)

        writer=csv.DictWriter(after,fieldnames=['first','last','house'])
        writer.writeheader()
        after={}
        for row in reader:
            last,first=row["name"].split(",")
            after={'first':first,'last':last,'house':row['house']}
            writer.writerow(after)
            

except FileNotFoundError:
    sys.exit(f"Couldn not read {sys.argv[1]}")
