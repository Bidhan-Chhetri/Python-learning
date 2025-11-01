import sys
import json
import requests

my_api = "000ac2bf7d48c49032517ba1797c21964f514003425a5955e6daf2c2b4c9aa39"
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + my_api)
    if len(sys.argv)  == 2:
        o = response.json()
        o["data"]["rank"] = str(sys.argv[1])
        amount = float(o["data"]["priceUsd"]) * float(o["data"]["rank"])
        print(f"${amount:,.4f}")
    elif len(sys.argv) == 1:
        print("Missing command line argument")


except ValueError:
    sys.exit("Command line argument is not a number")

except requests.RequestException:
    sys.exit("")