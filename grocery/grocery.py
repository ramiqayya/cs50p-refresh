grocery={}
while True:
    
    try:
        item=input()
        item=item.upper().strip()
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1
    except EOFError:
        break
    except KeyError:
        pass

sorted_grocery=sorted(grocery)
for item in sorted_grocery:
    print(grocery[item], item)
