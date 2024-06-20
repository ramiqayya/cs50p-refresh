from random import choice
import sys
import cowsay

# x=choice(["takeha", "Hadshi","Enta qadem ya man", "Lesh enta za3lan"])
# # print(x)
# y=choice([1,2,4,5,22,15])
# print(y)
disadvantages = {
    "enta qadem ya": "man is ensan",
    "koz I know?": "everything",
    "why like this": "because ej es ej",
    "takeha hena solha": "3lash hadshi",
}

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
