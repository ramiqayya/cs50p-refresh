
def main():

    while True:
        fraction=input("Fraction: ")
        
        per=convert(fraction)
        if per=="zero":
            continue
        else:
            print(gauge(per))
            break


def convert(fraction):
    
    try:

        x,y=fraction.split('/')
        x=int(x)
        y=int(y)
        
        if x > y:
            raise ValueError
        elif y==0:
            raise ZeroDivisionError
        else:
            return int((x/y)*100)
    
    except (ValueError,ZeroDivisionError):
        return "zero"
    


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()




    
