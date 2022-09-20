import json, bybitconfig
from flask import Flask, request, render_template
from math import *
from pybit.usdt_perpetual import HTTP



app = Flask(__name__)

client = HTTP("https://api.bybit.com",
               api_key=bybitconfig.BYBIT_API_KEY, api_secret=bybitconfig.BYBIT_API_SECRET)

def order(side,quantity, symbol,order_type="Market"):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order = client.place_active_order(
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=quantity,
            time_in_force="GoodTillCancel",
            reduce_only=False,
            close_on_trigger=False,
            position_idx=0)
                
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False
    return order

@app.route('/')#accueil
def welcome():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])#webhook tradingview
def webhook():
    #print(request.data)
    data = json.loads(request.data)
    
    if data['passphrase'] != bybitconfig.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }
    
    
    
    symbol= data['ticker'][:-4] #    supprime = PERP 
    
    side = data['strategy']['order_action'].capitalize()
    quantity = data['strategy']['order_contracts'] 
    order_response = order(side, quantity, symbol) 
    #print(symbol)
    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }
