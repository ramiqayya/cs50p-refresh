
def main():

    while True:

        fraction=input("Fraction: ")
        try:
            per=convert(fraction)
            
            print(gauge(per))
            break
        except (ValueError,ZeroDivisionError):
            pass



def convert(fraction):
    
 
    x,y=fraction.split('/')
    x=int(x)
    y=int(y)
    
    if y==0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return int((x/y)*100)
    
    
    


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()




    
