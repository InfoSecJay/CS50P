import requests
import json
import sys


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

def main():

    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1) # program needs to exit with code 1 which means ERROR

    try:
        x = float(sys.argv[1])
        results = response.json()
        price_usd = results["bpi"]["USD"]["rate_float"]
        price = price_usd * x
        print(f"${price:,}")
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
