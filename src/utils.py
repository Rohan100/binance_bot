from dotenv import load_dotenv
from binance.client import Client
load_dotenv()
import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# create a module-level client that other functions can reuse
# note: the original code used `testnet=True` so we preserve that behavior
client = Client(api_key=api_key, api_secret=api_secret, testnet=True)