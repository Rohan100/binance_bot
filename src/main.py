from limit_orders import limit_order_buy, limit_order_sell
from market_order import  place_buy_order, place_sell_order
import argparse

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Market Order Bot")

    # Define arguments
    parser.add_argument("symbol", type=str, help="Trading pair symbol (e.g. BTCUSDT)")
    parser.add_argument("side", type=str, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("quantity", type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Limit price for limit orders (optional)")

    # Parse arguments
    args = parser.parse_args()

    # Use them in your logic


    if args.price:
        if args.side == "BUY":
            limit_order_buy(args.symbol, args.quantity, args.price)
        else:
            limit_order_sell(args.symbol, args.quantity, args.price)
    else:
        if args.side == "BUY":
            order = place_buy_order(args.symbol, args.quantity)
            print(f"Market buy order placed: {order}")
        else:
            order = place_sell_order(args.symbol, args.quantity)
            print(f"Market sell order placed: {order}")



if __name__ == "__main__":
    main()


