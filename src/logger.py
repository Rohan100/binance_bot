# src/logger.py
import logging
import os

def setup_logger():
    # Define log file path (1 level up from src/)
    log_path = os.path.join(os.path.dirname(__file__), "../bot.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,  # you can change to DEBUG for more details
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
