
months={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

def main():
    while(True):

        try:

            date=input("Date: ")

            if ',' in date:
            
                month,day,year=date.split(' ')
                month=month.title()
                
                if month in months:
                    month= months[month]
                else:
                    raise ValueError
                
                day=int(day[:-1])
                
                year=int(year)
                
            
                check_day(day)
                
                print(f"{year}-{month:02}-{day:02}")
                break
            
            elif '/' in date:
                month, day, year= date.split('/')
                month =int(month)
                day=int(day)
                year=int(year)
                if month >12 or month <1:
                    raise ValueError
                check_day(day)

                print(f"{year}-{month:02}-{day:02}")
                break

            
        except ValueError:
            pass

def check_day(d):
    if 31<d or d<1:
        raise ValueError
    

    

main()