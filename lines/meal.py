def main():
    ...
    time= input("What time is it? ")

    hours,minutes=time.split(":")

    minutes=convert(minutes)
    newTime= float(hours)+minutes



    if  8 >= newTime >= 7:
        print("Breakfast time")
    elif  13 >= newTime >= 12:
        print("Lunch time")
    elif  19 >= newTime >= 18:
        print("Dinner time")
    



def convert(time):
    return float(time)/60


if __name__ == "__main__":
    main()


