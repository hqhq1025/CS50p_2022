import requests
import sys

try:
    num = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = o["bpi"]["USD"]["rate_float"]
    result = num * rate
    print(f"${result:,.4f}")
except requests.RequestException:
    print("Request error.")
except ValueError:
    sys.exit(1)
    #print("Value error.")
except IndexError:
    sys.exit(1)
    #print("Invalid input.")