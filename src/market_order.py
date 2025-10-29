
from typing import Optional, Dict, Any
from utils import client

def get_balance(asset: Optional[str] = None) -> Dict[str, Any]:

	try:
		account = client.get_account()
		balances = account.get("balances", [])

		parsed = {}
		for b in balances:
			symbol = b.get("asset")
			try:
				free = float(b.get("free", 0.0))
			except (TypeError, ValueError):
				free = 0.0
			try:
				locked = float(b.get("locked", 0.0))
			except (TypeError, ValueError):
				locked = 0.0

			total = free + locked
			# Only include non-zero balances in the default listing
			if total > 0:
				parsed[symbol] = {"free": free, "locked": locked, "total": total}

		if asset:
			return parsed.get(asset.upper(), {"free": 0.0, "locked": 0.0, "total": 0.0})

		return parsed
	except Exception as e:
		# Wrap Binance errors to provide clearer context to callers
		raise RuntimeError(f"Failed to fetch account balances: {e}") from e


def get_current_price(symbol: str) -> float:

    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])
        return price
    except Exception as e:
        raise RuntimeError(f"Failed to fetch current price for {symbol}: {e}") from e
	
def place_buy_order(symbol: str, quantity: float) -> Dict[str, Any]:

    try:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        return order
    except Exception as e:
        raise RuntimeError(f"Failed to place market order for {symbol}: {e}") from e

def place_sell_order(symbol: str, quantity: float) -> Dict[str, Any]:

    try:
        order = client.order_market_sell(
            symbol=symbol,
            quantity=quantity
        )
        return order
    except Exception as e:
        raise RuntimeError(f"Failed to place market order for {symbol}: {e}") from e

if __name__ == "__main__":
	# Simple demo when run directly. Do NOT commit API keys to source control.
	try:
		all_balances = get_balance()
		if not all_balances:
			print("No non-zero balances found.")
		else:
			for sym, val in all_balances.items():
				print(f"{sym}: free={val['free']}, locked={val['locked']}, total={val['total']}")
	except Exception as err:
		print(f"Error fetching balances: {err}")