import asyncio
import ccxt.pro
from asyncio import gather, run

global bid_prices
global ask_prices

bid_prices = {}
ask_prices = {}

async def symbol_loop(exchange, symbol):
    global bid_prices
    global ask_prices
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
            if best_diff_pct > -1:
                print(
                    f"{exchange.iso8601(now)}: Buy BTC/USDT on {min_ask_ex} ({min_ask_price}$), Sell BTC/USDT on {max_bid_ex} ({max_bid_price}$), Theorical profit + {round(best_diff_pct, 2)} %"
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
        "kucoin": ["BTC/USDT"],
        "binance": ["BTC/USDT"],
        "huobi": ["BTC/USDT"],
        "bitget": ["BTC/USDT"],
        "cryptocom": ["BTC/USDT"],
        
    }
    loops = [
        exchange_loop(exchange_id, symbols)
        for exchange_id, symbols in exchanges.items()
    ]
    try:
        await asyncio.wait_for(gather(*loops), timeout=45.0)
    except asyncio.TimeoutError:
        print("Exited after 45 seconds")

run(main())
