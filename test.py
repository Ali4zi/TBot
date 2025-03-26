from tradingview_ta import TA_Handler, Interval, Exchange
import datetime
from bingX import *
from time import sleep


# # Define the handler for BTCUSDT
# btc_usdt_1H = TA_Handler(
#     symbol="BTCUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_1_HOUR  # You can change the interval as needed
# )
# btc_usdt_15Min = TA_Handler(
#     symbol="BTCUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_15_MINUTES  # You can change the interval as needed
# )
# btc_usdt_5Min = TA_Handler(
#     symbol="BTCUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_5_MINUTES  # You can change the interval as needed
# )
# usdt_d = TA_Handler(
#     symbol="EURUSDT",
#     screener="crypto",
#     exchange="BINANCE",
#     interval=Interval.INTERVAL_5_MINUTES  # You can change the interval as needed
# )


# Connect to bingX
my_api_key = "3J1lRzlqSVbOphcF1B9YhWtbbQTYwTUJuVKVErreStAnSpl8RIOqZytwyMmSBMD6G03hSR3t3biG8QHRbAQ"
my_api_secret = "BHmOrXrhDXKADMyY6L0b9drtuHxJ9KcTvj5HkA53h6IJwIR3jl9GAhXXd5HzkBFpgy5EXK8wHK8t23qLw"
bingx_client = BingX(api_key=my_api_key, secret_key=my_api_secret)
try:
    # Get the symbol and last price of BTC/USDT
    response = bingx_client.perpetual_v2.market.get_ticker(symbol="BTC-USDT")
    symbol = response["symbol"]
    last_price = response["lastPrice"]
    print(symbol, last_price)

# Call the Trade API of Perpetual V2
    # bingx_client.perpetual_v2.trade.create_order(Order(symbol="DOGE-USDT", side=Side.BUY, positionSide=PositionSide.LONG, quantity=100.0))
    ac_det=bingx_client.standard.get_account_details()
    print(ac_det)
except (ClientError, ServerError) as e:
    error_code = e.error_code
    error_message = e.error_message

# sleep(30)

# try:
#     response = bingx_client.perpetual_v2.trade.open_order(symbol="BTC-USDT", side="BUY", quantity=0.001, price=last_price)
#     print(response)
# except (ClientError, ServerError) as e:
#     error_code = e.error_code
#     error_message = e.error_message

## Get the analysis
# analysis_1H = btc_usdt_1H.get_analysis()
# analysis_15Min = btc_usdt_15Min.get_analysis()
# analysis_5Min = btc_usdt_5Min.get_analysis()
#analysis_usdt_d = usdt_d.get_analysis()

# # Print the analysis
# print(datetime.datetime.now())
# print("Symbol:", analysis_usdt_d.symbol)
# print("Exchange:", analysis_usdt_d.exchange)
# print("Interval:", analysis_usdt_d.interval)
# print("Recommendation:", analysis_usdt_d.summary["RECOMMENDATION"])
# print("Buy:", analysis_usdt_d.summary["BUY"])
# print("Sell:", analysis_usdt_d.summary["SELL"])
# print("Neutral:", analysis_usdt_d.summary["NEUTRAL"])

# # imp. indicators
# indi = ["close","open","high","low","volume"]
# # Print the indicators
# print("\nIndicators:")
# for indicator in analysis_usdt_d.indicators:
#     if indicator in indi:
#         print(indicator, ":", analysis_usdt_d.indicators[indicator])