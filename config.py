import os

# from constants import routers, tokens


def __getattr__(_):
    return None


BLOCKNATIVE_KEY = os.getenv("BLOCKNATIVE_KEY")

# RPC_URL = "https://bsc-dataseed.binance.org/"

# ROUTER = routers.PANCAKESWAP

# BUY_TIMES = 1

# GAS_LIMIT = 300000

# GAS_PRICE_MULTIPLIER = 1

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# TO_ADDRESS = ""

# FROM_TOKEN = ""

FROM_TOKEN_AMOUNT = 0.001

TO_TOKEN = ""

# TO_TOKEN_AMOUNT_MIN = 0
