import requests
import os
from flask import Flask, render_template
from collections import OrderedDict

api_key = os.environ.get("tracker_key")
URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
app = Flask("__name__")

headers = {"X-CMC_PRO_API_KEY": api_key,
           'Accepts': 'application/json',
           }
params = {
           "slug": "bitcoin,ethereum,cardano,bnb,xrp,solana,dogecoin,tron,chainlink,polygon,"
                   "avalanche,polkadot,cosmos,stellar,hedera,aptos,singularitynet"

}

# Request data from API
request = requests.get(url=URL, headers=headers, params=params)
data = request.json()
data = data["data"]
sorted_data = OrderedDict(sorted(data.items(), key=lambda x: x[1]["quote"]["USD"]["market_cap"], reverse=True))


@app.route("/")
def home():
    return render_template("index.html", data=sorted_data)


if __name__ == "__main__":
    app.run(debug=True)
