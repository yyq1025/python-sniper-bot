import sys
from web3 import Web3
import config


def get_blocknative_key() -> str:
    if not config.BLOCKNATIVE_KEY:
        print("invalid blocknative key")
        sys.exit(1)
    return config.BLOCKNATIVE_KEY


def get_rpc_url() -> str:
    return config.RPC_URL or "https://bsc-dataseed.binance.org/"


def get_router() -> str:
    if not Web3.isAddress(config.ROUTER):
        print("invalid router address")
        sys.exit(1)
    return config.ROUTER


def get_buy_times() -> int:
    return config.BUY_TIMES or 5


def get_gas_limit() -> int:
    return config.GAS or 300000


def get_gas_price_multiplier() -> int:
    return config.GAS_PRICE_MULTIPLIER or 1


def get_private_key() -> str:
    if not config.PRIVATE_KEY:
        print("invalid private key")
        sys.exit(1)
    return config.PRIVATE_KEY


def get_to_address() -> str:
    if config.TO_ADDRESS and not Web3.isAddress(config.TO_ADDRESS):
        print("invalid to address")
        sys.exit(1)
    return config.TO_ADDRESS


def get_from_token() -> str:
    if not Web3.isAddress(config.FROM_TOKEN):
        print("invalid from token address")
        sys.exit(1)
    return config.FROM_TOKEN


def get_from_token_amount() -> int:
    if not config.FROM_TOKEN_AMOUNT:
        print("invalid from token amount")
        sys.exit(1)
    return config.FROM_TOKEN_AMOUNT


def get_to_token() -> str:
    if not Web3.isAddress(config.TO_TOKEN):
        print("invalid to token address")
        sys.exit(1)
    return config.TO_TOKEN


def get_to_token_amount_min() -> int:
    return config.TO_TOKEN_AMOUNT_MIN or 0
