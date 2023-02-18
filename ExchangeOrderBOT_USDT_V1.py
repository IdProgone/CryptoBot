import asyncio
import ccxt.pro
#import ccxt
import time
from asyncio import gather, run

class SpotBitget():
    def __init__(self, apiKey=None, secret=None, password=None):
        bitgetAuthObject = {
            "apiKey": apiKey,
            "secret": secret,
            "password": password,
        }
        if bitgetAuthObject['secret'] == None:
            self._auth = False
            self._session = ccxt.bitget()
        else:
            self._auth = True
            self._session = ccxt.bitget(bitgetAuthObject)
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
        self._session.options['createMarketBuyOrderRequiresPrice'] = False
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

    @authentication_required
    def get_balance(self, symbol):
        try:
            balances = self._session.fetch_balance()
            balance = balances[symbol.split("/")[0]]
            return balance
        except Exception as err:
            raise err

class SpotBinance():
    def __init__(self, apiKey=None, secret=None, password=None):
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
        self._session.options['createMarketBuyOrderRequiresPrice'] = False
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

    @authentication_required
    def get_balance(self, symbol):
        try:
            balances = self._session.fetch_balance()
            balance = balances[symbol.split("/")[0]]
            return balance
        except Exception as err:
            raise err

class SpotKucoin():
    def __init__(self, apiKey=None, secret=None, password=None):
        kucoinAuthObject = {
            "apiKey": apiKey,
            "secret": secret,
            "password": password,
        }
        if kucoinAuthObject['secret'] == None:
            self._auth = False
            self._session = ccxt.kucoin()
        else:
            self._auth = True
            self._session = ccxt.kucoin(kucoinAuthObject)
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
        self._session.options['createMarketBuyOrderRequiresPrice'] = False
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

    @authentication_required
    def get_balance(self, symbol):
        try:
            balances = self._session.fetch_balance()
            balance = balances[symbol.split("/")[0]]
            return balance
        except Exception as err:
            raise err

class SpotHuobi():
    def __init__(self, apiKey=None, secret=None, password=None):
        huobiAuthObject = {
            "apiKey": apiKey,
            "secret": secret,
        }
        if huobiAuthObject['secret'] == None:
            self._auth = False
            self._session = ccxt.huobi()
        else:
            self._auth = True
            self._session = ccxt.huobi(huobiAuthObject)
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
        self._session.options['createMarketBuyOrderRequiresPrice'] = False
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

    @authentication_required
    def get_balance(self, symbol):
        try:
            balances = self._session.fetch_balance()
            balance = balances[symbol.split("/")[0]]
            return balance
        except Exception as err:
            raise err

huobi = SpotHuobi(
    apiKey="",
    secret="",
)
kucoin = SpotKucoin(
    apiKey="",
    secret="",
    password=""
)
binance = SpotBinance(
    apiKey="",
    secret=""
)
bitget = SpotBitget(
    apiKey="",
    secret="",
    password=""
)

global bid_prices
global ask_prices
global min_ask_ex
global min_ask_price
global max_bid_ex
global max_bid_price

bid_prices = {}
ask_prices = {}
min_ask_ex = {}
min_ask_price = {}
max_bid_ex = {}
max_bid_price = {}

async def symbol_loop(exchange, symbol):
    global bid_prices
    global ask_prices
    global min_ask_ex
    global min_ask_price
    global max_bid_ex
    global max_bid_price
    print("Starting the", exchange.id, "symbol loop with", symbol)
    while True:
        try:
            orderbook = await exchange.watch_order_book(symbol)
            now = exchange.milliseconds()
            bid_prices[exchange.id] = orderbook["bids"][0][0]
            ask_prices[exchange.id] = orderbook["asks"][0][0]
            min_ask_ex = min(ask_prices, key=ask_prices.get)
            max_bid_ex = max(bid_prices, key=bid_prices.get)
            min_ask_price = ask_prices[min_ask_ex]
            max_bid_price = bid_prices[max_bid_ex]
            best_diff = max_bid_price - min_ask_price
            best_diff_pct = ((max_bid_price - min_ask_price) / min_ask_price) * 100
            if best_diff_pct > 0.4:
                print(
                    f"{exchange.iso8601(now)}: Buy USDT/XXX on {min_ask_ex} ({min_ask_price}$), Sell USDT/XXX on {max_bid_ex} ({max_bid_price}$), Theorical profit + {round(best_diff_pct, 2)} %"
                )
        except Exception as e:
            print(str(e))
            break

async def exchange_loop(exchange_id, symbols):
    print("Starting the", exchange_id, "exchange loop with", symbols)
    exchange = getattr(ccxt.pro, exchange_id)()
    loops = [symbol_loop(exchange, symbol) for symbol in symbols]
    await gather(*loops)
    await exchange.close()

async def main():
    exchanges = {
        
        "binance": ["USDT/XXX"],
        #"kucoin": ["USDT/XXX"],
        "bitget": ["USDT/XXX"],
        "huobi": ["USDT/XXX"],
        
    }
    loops = [
        exchange_loop(exchange_id, symbols)
        for exchange_id, symbols in exchanges.items()
    ]
    try:
        await asyncio.wait_for(gather(*loops), timeout=15.0)
    except asyncio.TimeoutError:
        print("Exited after 15 seconds")

run(main())


exchanges = [ccxt.binance(), ccxt.huobi(), ccxt.bitget()]
symbol = "USDT/XXX"
#amount = 20
## Calculer la quantité de usdta Inu à vendre en pourcentage
#percentage = float(input("Entrez le pourcentage en vente (en décimal) : "))
#usdt_to_sell = usdt_balance * percentage
amount = float(input("Nombre d'unité en USDT: "))

print("Prix d' Achat actuel de la Paire :", symbol, "- R$", min_ask_price, "sur", min_ask_ex)
print("Prix de Vente actuel de la Paire :", symbol, "- R$", max_bid_price, "sur", max_bid_ex)

print(f"Prix d'achat le plus bas : {min(ask_prices.values())} sur {min(ask_prices, key=ask_prices.get)}")
print(f"Prix de vente le plus élevé : {max(bid_prices.values())} sur {max(bid_prices, key=bid_prices.get)}")

# Initialiser les variables de suivi des prix
min_ask_price = float("inf")
max_bid_price = float("-inf")
min_ask_ex = None
max_bid_ex = None

# Parcourir la liste des exchanges et récupérer les prix
for exchange in exchanges:
    # Récupérer le ticker pour le symbole
    ticker = exchange.fetch_ticker(symbol)
    # Récupérer le prix d'achat actuel pour l'exchange
    ask_price = ticker["ask"]
    bid_price = ticker["bid"]
    # Vérifier si c'est le prix le plus bas jusqu'à présent
    if ask_price < min_ask_price:
        min_ask_price = ask_price
        min_ask_ex = exchange.id
    if bid_price > max_bid_price:
        max_bid_price = bid_price
        max_bid_ex = exchange.id

# Acheter à l'exchange avec le prix le plus bas
if min_ask_ex is not None:
    # Récupérer l'objet de l'exchange avec le prix d'achat le moins cher
    if min_ask_ex == 'binance':
        exchange_buy = binance
    elif min_ask_ex == 'huobi':
        exchange_buy = huobi
    elif min_ask_ex == 'bitget':
        exchange_buy = bitget
    else:
        print(f"Erreur : Exchange {min_ask_ex} non pris en charge.")
        exit()

    # Passer l'ordre limit d'achat
    exchange_buy.place_limit_order(symbol, 'buy', amount, min_ask_price)
    #exchange_buy.place_market_order(symbol, 'buy', amount)
    print(f"Ordre d'achat passé sur {min_ask_ex} pour {amount} {symbol} à {min_ask_price}")
    ticker = exchange.fetch_ticker(symbol)
    market_price = ticker["ask"]
    print(f'---> Ordre du cours sur: {min_ask_ex }, Symbol: {symbol}, Side: |]Achat[|, Quantity: {amount}, Price: R$ {market_price}')
else:
    print("Aucun exchange trouvé avec des prix d'achat pour la paire de devises.")

# Vendre à l'exchange avec le prix le plus élevé
if max_bid_ex is not None:
    # Récupérer l'objet de l'exchange avec le prix de vente le plus élevé
    if max_bid_ex == 'binance':
        exchange_sell = binance
    elif max_bid_ex == 'huobi':
        exchange_sell = huobi
    elif max_bid_ex == 'bitget':
        exchange_sell = bitget
    else:
        print(f"Erreur : Exchange {max_bid_ex} non pris en charge.")
        exit()

    # Passer l'ordre limit de vente
    exchange_sell.place_limit_order(symbol, 'sell', amount, max_bid_price)
    #exchange_sell.place_market_order(symbol, 'sell', amount)
    print(f"Ordre de vente passé sur {max_bid_ex} pour {amount} {symbol} à {max_bid_price}")
    ticker = exchange.fetch_ticker(symbol)
    market_price = ticker["ask"]
    print(f'---> Ordre du cours sur: {max_bid_ex }, Symbol: {symbol}, Side: ||Vente||, Quantity: {amount}, Price: R$ {market_price}')
else:
    print("Aucun exchange trouvé avec des prix de vente pour la paire de devises.")

open_orders = exchange_buy._session.fetch_open_orders(symbol)
for order in open_orders:
    symbol = order['symbol']
    side = order['side']
    number = order['amount']
    prix = order['price']
    datetime = order['datetime']
    print(f'///Ordre en cours sur:, {min_ask_ex }, datetime: {datetime}, Symbol: {symbol}, Side: {side}, Quantity: {number}, Price: R$ {prix}|||')

open_orders = exchange_sell._session.fetch_open_orders(symbol)
for order in open_orders:
    symbol = order['symbol']
    side = order['side']
    number = order['amount']
    prix = order['price']
    datetime = order['datetime']
    print(f'*** Ordre en cours sur:, {max_bid_ex },datetime: {datetime}, Symbol: {symbol}, Side: {side}, Quantity: {number}, Price: R$ {prix}***')

usdt_balance_buy = exchange_buy.get_balance("USDT")["free"]
xxx_balance_buy = exchange_buy.get_balance("xxx")["free"]

usdt_balance_sell = exchange_sell.get_balance("USDT")["free"]
xxx_balance_sell = exchange_sell.get_balance("xxx")["free"]
print("$$$ Exchange",min_ask_ex ,"--- Reste", usdt_balance_buy, "$ & R$", xxx, "sur le compte")
print("$$$ Exchange", max_bid_ex,"--- Reste", usdt_balance_sell, "$ & R$", xxx_balance_sell, "sur le compte")

input("Appuyez sur Entrée pour fermer le script.") 
