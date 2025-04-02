# Connect to bingX
from bingX import *

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

    # try:
#     response = bingx_client.perpetual_v2.trade.open_order(symbol="BTC-USDT", side="BUY", quantity=0.001, price=last_price)
#     print(response)
# except (ClientError, ServerError) as e:
#     error_code = e.error_code
#     error_message = e.error_message