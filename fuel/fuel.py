while(True):
    try:
        fraction=input("Fraction: ")

        y,x=fraction.split('/')
        y=int(y)
        x=int(x)

        per= (int(y)/int(x))*100
        if y > x or x<0 or y<0:
            continue
        elif 99<=per<=100:
            print("F")
            break
        elif 0<=per<=1:
            print("E")
            break
        elif 1<per<99:
            print(f"%{int(per)}")
            break
    except (ValueError,ZeroDivisionError):
        pass
