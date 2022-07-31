from math import *
from pybit import usdt_perpetual
from pybit.usdt_perpetual import HTTP
import bybitconfig




client = usdt_perpetual.HTTP("https://api-testnet.bybit.com",
               api_key=bybitconfig.TESTNET_API_KEY, api_secret=bybitconfig.TESTNET_API_SECRET)


print(client.position_mode_switch(
    symbol="BTCUSDT",
    mode="MergedSingle"
))



