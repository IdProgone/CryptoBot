import asyncio
import ccxt.pro
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

bitget = SpotBitget(
    apiKey="",
    secret="",
    password=""
)

exchange = ccxt.bitget()
symbol = "USDT/XXX"
usdt_balance = bitget.get_balance("USDT")["free"]
xxx_balance = bitget.get_balance("XXX")["free"]
ticker = exchange.fetch_ticker(symbol)
market_price = ticker['last']  # prix de marché
price_bid = ticker['bid']
print("Prix actuel de la Paire en Achat:", symbol, "- R$", ticker['bid'], "sur Bitget")
print("Prix actuel de la Paire en Vente :", symbol, "- R$", ticker['last'], "sur Bitget")
print("Votre solde actuel:", bitget.get_balance("USDT")["free"], "USDT", "&", bitget.get_balance("XXX")["free"], "XXX")
print("Vos Ordres en cours:")
open_orders = bitget._session.fetch_open_orders(symbol)
for order in open_orders:
    symbol = order['symbol']
    side = order['side']
    number = order['amount']
    prix = order['price']
    datetime = order['datetime']
    print(f'datetime: {datetime}, Symbol: {symbol}, Side: {side}, Quantity: {number}, Price: R$ {prix}')

while True:
    side = input("'B' to buy, 'S' to sell, type 'R' to refresh the price or 'Q' for quit: ") 
    if side.lower() == 'r':
        symbol = 'USDT/XXX'
        ticker = exchange.fetch_ticker(symbol)
        market_price = ticker['last']
        print("Prix marché rafraîchi en Achat:", symbol, "- R$", ticker['bid'], "sur Bitget")
        print("Prix marché rafraîchi en Vente :", symbol, "- R$", ticker['last'], "sur Bitget")
        continue

    if side.lower() not in ['b', 's', 'r', 'q']:
        print("Entrée non valide, veuillez entrer 'b' pour buy ou 's' pour sell, ou tapez 'r' pour rafraîchir le prix pu 'q' pour quitter.")
        continue

    amount = float(input("Nombre d'unité en USDT: "))

    if side.lower() == 's':
        symbol = 'USDT/XXX'  # ou tout autre paire de trading
        ticker = exchange.fetch_ticker(symbol)  # récupération du ticker du marché
        market_price = ticker['last']  # prix de marché
        side = 'sell'
        bitget.place_limit_order(symbol, side, amount, market_price )
        print(f"Ordre de limite de vente de {amount} {symbol} au prix de R$ ({market_price}) a été placé avec succès.")
    elif side.lower() == 'b':
        symbol = 'USDT/XXX'  # ou tout autre paire de trading
        ticker = exchange.fetch_ticker(symbol)  # récupération du ticker du marché
        price_bid = ticker['bid']
        side = 'buy'
        bitget.place_limit_order(symbol, side, amount, price_bid )
        print(f"Ordre limite d'achat de {amount} {symbol} à {price_bid} R$ a été placé avec succès.")
         
    elif side.lower() == 'q':
        break      
    while True:
        try:
            break
        except Exception as err:
            print(err)
            if str(err) == "bitget does not have market symbol " + symbol:
                time.sleep(0.2)
            pass 
    usdt_balance_1 = bitget.get_balance("USDT")["free"]
    xxx_balance_1 = bitget.get_balance("XXX")["free"]
    if side.lower() == 'buy':
        print( side, "Order success!","Acheté au prix de : R$", price_bid, " - ", amount, "USDT" , side,"--- Reste", usdt_balance_1, "$ & R$", xxx_balance_1, "sur le compte")
    if side.lower() == 'sell':
        print( side, "Order success!","Vendu au prix de : R$", market_price, " - ", amount, "USDT" , side,"--- Reste", usdt_balance_1, "$ & R$", xxx_balance_1, "sur le compte")
        print("Ordre en cours:")
    open_orders = bitget._session.fetch_open_orders(symbol)
    for order in open_orders:
        symbol = order['symbol']
        side = order['side']
        quantity = order['amount']
        prix_2 = order['price']
        datetime = order['datetime']
        print(f'datetime: {datetime}, Symbol: {symbol}, Side: {side}, Quantity: {quantity}, Price: R$ {prix_2}')
    input("Appuyez sur Entrée pour continuer le script.")   

    

