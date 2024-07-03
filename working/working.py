import re
import sys


def main():
    
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("Value Error!")
  

def convert(s):
    pattern=r"^(.+) (AM|PM) to (.+) (AM|PM)$"
    try:
        matches=re.search(pattern,s,re.IGNORECASE)
        startt=matches.group(1)
        start_t=matches.group(2)
        endt=matches.group(3)
        endt_t=matches.group(4)
    except(ValueError,AttributeError):
        raise ValueError

    
    if start_t =="AM":
        time1 =time_converter_AM(startt)
    elif start_t=="PM":
        time1=time_converter_PM(startt)
    
    if endt_t =="AM":
        time2 =time_converter_AM(endt)
    elif endt_t=="PM":
        time2=time_converter_PM(endt)
    return f"{time1} to {time2}"
 
    

    

    
def time_converter_PM(time):
    if ":" in time:
        hr,min=time.split(":")
        if int(min)>=60 or int(hr)>12:
            raise ValueError
        time_h=int(hr)+12
        return f"{time_h}:{int(min):02}"
    else:
        time_h=int(time)+12
        return f"{time_h}:00"

def time_converter_AM(time):

    if ":" in time:
  
        hr,min= time.split(":")
       
        if int(hr)>12 or int(min)>=60:
          
            raise ValueError
        return f"{int(hr):02}:{int(min):02}"
    else:
        if int(time)>12:
            raise ValueError
        return f"{int(time):02}:00"









if __name__ == "__main__":
    main()