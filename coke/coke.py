
coins=[5,10,25]

amount_due=50
while True:
    print(f"Amount Due: {amount_due}")
    amount=int(input("insert coin: "))

    if amount in coins:
        amount_due-=amount
        if amount_due <= 0:
            break
        # print(f"Amount Due: {amount_due}")

print(f"Change Owed: {-1*amount_due}")




