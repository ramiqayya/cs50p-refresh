import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    nos=float(sys.argv[1])

    

    x=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    object=x.json()
    # print(object["bpi"]["USD"]["rate_float"])
    price=nos*object["bpi"]["USD"]["rate_float"]

    print(f"${price:,.4f}") 
except (requests.RequestException, ValueError ):
    sys.exit("Command-line argument is not a number")


