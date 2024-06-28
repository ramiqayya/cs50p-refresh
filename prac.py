from random import choice
import sys
import csv
import cowsay
ddrt=[]
# with open("marawan.csv") as file:
#     for line in file:
#         col1,col2,col3=line.rstrip().split(',')
#         ddr={"col1":col1, "col2":col2, "col3":col3}
#         ddrt.append(ddr)

with open("marawan.csv") as file:
    reader=csv.reader(file)
    for zeze,umteezi,mazef in reader:
        ddrt.append({"zeze":zeze, "umteezi":umteezi,"mazef":mazef})



for ddr in sorted(ddrt, key=lambda mashi:mashi["zeze"]):     
    print(f'{ddr["zeze"]}--{ddr["umteezi"]}--{ddr["mazef"]}')


# x=choice(["takeha", "Hadshi","Enta qadem ya man", "Lesh enta za3lan"])
# # print(x)
# y=choice([1,2,4,5,22,15])
# print(y)
# disadvantages = {
#     "enta qadem ya": "man is ensan",
#     "koz I know?": "everything",
#     "why like this": "because ej es ej",
#     "takeha hena solha": "3lash hadshi",
# }

# if len(sys.argv) == 2:
#     cowsay.trex("Hello, " + sys.argv[1])
