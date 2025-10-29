from market_order import get_current_price, place_buy_order, place_sell_order
import time
def limit_order_buy(symbol,quantity,price):
    while True:
        print("Checking price for limit buy order...")
        try:
            current_price = get_current_price(symbol)
            if current_price <= price:
                order = place_buy_order(symbol, quantity)
                print(f"Limit buy order placed: {order}")
                return
        except Exception as e:
            print(f"Error placing limit buy order: {e}. Retrying...")
            time.sleep(1)

        time.sleep(5)  # Check every 5 seconds

def limit_order_sell(symbol,quantity,price):
    while True:
        print("Checking price for limit sell order...")
        try:
            current_price = get_current_price(symbol)
            if current_price >= price:
                order = place_sell_order(symbol, quantity)
                print(f"Limit sell order placed: {order}")
                return
        except Exception as e:
            print(f"Error placing limit sell order: {e}. Retrying...")
            time.sleep(1)

        time.sleep(5)  # Check every 5 seconds