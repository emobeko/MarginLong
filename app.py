from flask import Flask, request
import json
from binance.spot import Spot as Client


app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']

        params = {
            "asset": ticker,
            "amount": quantity,
        }

        params2 = {
            "symbol": ticker,
            "side": "BUY",
            "type": "MARKET",
            "quantity": quantity,
        }

        Client(binanceApiKey, binanceSecretKey).margin_borrow(**params)
        Client(binanceApiKey, binanceSecretKey).new_margin_order(**params2)



    except:
        pass
    return {
        "code": "success",
    }










