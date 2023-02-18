import ccxt
import time

class Spotbinance():
    def __init__(self, apiKey=None, secret=None):
        binanceAuthObject = {
            "apiKey": apiKey,
            "secret": secret,
        }
        if binanceAuthObject['secret'] == None:
            self._auth = False
            self._session = ccxt.binance()
        else:
            self._auth = True
            self._session = ccxt.binance(binanceAuthObject)
        self.market = self._session.load_markets()

    def reload_markets(self):
        self.market = self._session.load_markets()

    def authentication_required(fn):
        """Annotation for methods that require auth."""
        def wrapped(self, *args, **kwargs):
            if not self._auth:
                print("You must be authenticated to use this method", fn)
                exit()
            else:
                return fn(self, *args, **kwargs)
        return wrapped

    def convert_amount_to_precision(self, symbol, amount):
        return self._session.amount_to_precision(symbol, amount)

    def convert_price_to_precision(self, symbol, price):
        return self._session.price_to_precision(symbol, price)

    @authentication_required
    def place_market_order(self, symbol, side, amount):
        try:
            return self._session.createOrder(
                symbol, 
                'market', 
                side, 
                self.convert_amount_to_precision(symbol, amount),
                None
            )
        except Exception as err:
            raise err

    @authentication_required
    def place_limit_order(self, symbol, side, amount, price):
        try:
            return self._session.createOrder(
                symbol, 
                'limit', 
                side, 
                self.convert_amount_to_precision(symbol, amount), 
                self.convert_price_to_precision(symbol, price)
                )
        except Exception as err:
            raise err

binance = Spotbinance(
    apiKey="",
    secret=""
)

#symbol = "SHIB/USDT"
amount = 665000
seconds_before_sell = 60

while True:
    try:
        binance.reload_markets()

        binance.place_market_order(symbol, "buy", amount)
        print("Buy Order success!")

        print("Waiting for sell...")
        time.sleep(seconds_before_sell)

        binance.place_market_order(symbol, "sell", amount)
        print("Sell Order success!")

        break
    except Exception as err:
        print(err)
        if str(err) == "binance does not have market symbol " + symbol:
            time.sleep(0.2)
        pass
