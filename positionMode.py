from math import *
from pybit import usdt_perpetual
from pybit.usdt_perpetual import HTTP
import bybitconfig




client = usdt_perpetual.HTTP("https://api-testnet.bybit.com",
               api_key=bybitconfig.BYBIT_API_KEY, api_secret=bybitconfig.BYBIT_API_SECRET)


print(client.position_mode_switch(
    symbol="BTCUSDT",
    mode="MergedSingle"
))



