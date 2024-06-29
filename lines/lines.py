import sys

if len(sys.argv)>2:
    sys.exit("Too many arguments")
elif len(sys.argv)<2:
    sys.exit("Too few arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")


try:
    with open(sys.argv[1]) as file:
        reader=file.readlines()
        counter=0
        for row in reader:
            if row.lstrip().startswith("#"):
                pass
            elif len(row.lstrip())==0:
                pass
            else:
                counter+=1
        print(counter)        


except (FileNotFoundError):
    sys.exit("File not Found")