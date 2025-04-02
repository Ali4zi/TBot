from tradingview_ta import * 
from datetime import *
import math
from time import *
import pandas as pd
#pip install python-binance
from binance.client import Client
import time
#Connect Binance
API_Key= "1GqW8CehdaYaCsVhJPss1OcbUtBDKeJiGZY7UZFffKyIgYW450MwibONb99K3oY9"
Secret_Key= "mhtqeGnKcw766Hbj2m1VpgV6TEg3PI0p91ZdhuKtcOnAo7XC7X4Y544v3Lc2zfnZ"

client = Client(API_Key,Secret_Key,testnet= True)
client.get_account()
#Profit - Risk
exp = 5 

#History P&R
tp = 10

#trend
trend = 0

# Position Test
pos = +5



# Read History
df = pd.read_excel(r"C:\Users\AliRezaAzari\OneDrive - Provadis Hochschule\TBot\History.xlsx")
# # gv = df['G&V'].iloc[-1]
# print(df.head())

# Define the handler for BTCUSDT
btc_usdt_1H = TA_Handler(
    symbol="BTCUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_1_HOUR  # You can change the interval as needed
)
# btc_usdt_15Min = TA_Handler(
#     symbol="BTCUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_15_MINUTES  # You can change the interval as needed
# )
btc_usdt_5Min = TA_Handler(
    symbol="BTCUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_5_MINUTES  # You can change the interval as needed
)
# usdt_d = TA_Handler(
#     symbol="EURUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_5_MINUTES  # You can change the interval as needed
# )




#sleep(1)

#trend


# Get the analysis
# analysis_1H = btc_usdt_1H.get_analysis()
# analysis_15Min = btc_usdt_15Min.get_analysis()
analysis_5Min = btc_usdt_5Min.get_analysis()
#analysis_usdt_d = usdt_d.get_analysis()

## oscillators_analys = btc_usdt_1H.analysis.indicator["open"]
## print(oscillators_analys)
##analysis_5min = get_multiple_analysis(screener="crypto", interval=Interval.INTERVAL_5_MINUTES, symbols=["BINANCE:BTCUSDT", "BINANCE:EURUSDT"])


# # Print the analysis
# print(datetime.datetime.now())
# print("Symbol:", analysis_usdt_d.symbol)
# print("Exchange:", analysis_usdt_d.exchange)
# print("Interval:", analysis_usdt_d.interval)
# print("Recommendation:", analysis_usdt_d.summary["RECOMMENDATION"])
# print("Buy:", analysis_usdt_d.summary["BUY"])
# print("Sell:", analysis_usdt_d.summary["SELL"])
# print("Neutral:", analysis_usdt_d.summary["NEUTRAL"])
#print(analysis_5min["BINANCE:BTCUSDT"].summary)

# imp. indicators
# indi = ["ADX","open","high","low","volume",]
# # Print the indicators
# print("\nIndicators:")
# for indicator in analysis_5Min.indicators:
#     #if indicator in indi:
#         print(indicator, ":", analysis_5Min.indicators[indicator])
def closePos():
    global tp
    global pos

    if(pos >= tp):
        pos  = 0
    else:
        tp += abs(pos)
    
    if (math.isnan(df['Close'].iloc[-1]) and not(df['Open'].iloc[-1])):
        df.loc[len(df), 'Close'] = analysis_5Min.indicators["open"]
        df.loc[len(df), 'DateTime C']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
# Indicator Signal
def buy_signal(): 
    return analysis_5Min.indicators["ADX"] > 20 or analysis_5Min.indicators["EMA10"] >= analysis_5Min.indicators["low"] or analysis_5Min. indicators["RSI"] > 70 or analysis_5Min. indicators["RSI[1]"] > 70

def sell_signal():
    return analysis_5Min.indicators["ADX"] > 20 or analysis_5Min.indicators["EMA10"] <= analysis_5Min.indicators["high"] or analysis_5Min. indicators["RSI"] < 30 or analysis_5Min. indicators["RSI[1]"] < 30
    
def openPos():
            
            df.loc[len(df), 'Open'] = analysis_5Min.indicators["open"]
            df.loc[len(df)-1, 'DateTime O'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df.loc[len(df)-1, 'Symbol'] = analysis_5Min.symbol



def trend_find():
    global trend
    trend = 1 if(analysis_5Min.indicators["EMA10"]> analysis_5Min.indicators["EMA20"] > analysis_5Min.indicators["EMA100"]) else -1

def gv_cal(tp_rech):
    global tp
    global exp

    if(tp == 0):
        return exp/tp_rech
    else:
        return (tp + exp) / tp_rech

# print(gv_cal(2))
# # print(gv_cal())
# #openPos()
# closePos()
# df.to_excel(r"C:\Users\AliRezaAzari\OneDrive - Provadis Hochschule\TBot\History.xlsx", index=False)
# print(df)
# trend_find()
# print(trend)