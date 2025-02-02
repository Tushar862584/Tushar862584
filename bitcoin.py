import sys
import requests
if len(sys.argv)==2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument  ")
    sys.exit(1)

try:
       X=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
       output =X.json()
       bitcoin = output["bpi"]["USD"]["rate_float"]
       amount=bitcoin*value
       print(f"${amount:,.4f}")
except requests.RequestException:
      print("RequestException")
      sys.exit(1)



