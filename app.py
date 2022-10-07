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
    print(data)
    
    if data['passphrase'] != bybitconfig.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }
    order_id = data['strategy']['order_id'] 
    if data['exchange'] == 'BINANCE':
        symbol= data['ticker'][:-4] #delete PERP on ticker form Binance TV chart (BTCUSDTPERP = BTCUSDT)
    else:
        symbol = data['ticker'] 
    
    side = data['strategy']['order_action'].capitalize()
    quantity = data['strategy']['order_contracts']
    
    #Close position if SL signal or open trade
    if order_id == "Short SL":
        print("Close Short Position : SL")
        order_response = client.close_position(symbol)
    elif order_id == "Long SL":
        print("Close Long Position : SL")
        order_response = client.close_position(symbol)
    else:
        print('Entry')
        order_response = order(side, quantity, symbol)
    
    #Get trade info
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
    
