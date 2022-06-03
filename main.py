import json
import websocket
from threading import Thread
from web3 import Web3
from helper import wrapper
from helper.abis import ERC20_ABI, UNISWAP_ABI
from helper.constants import WBNB
from helper.blocknative_config import required_params, init, watch, filter_config

rpc_url = wrapper.get_rpc_url()

router = wrapper.get_router()

buy_times = wrapper.get_buy_times()

gas_limit = wrapper.get_gas_limit()

gas_price_multiplier = wrapper.get_gas_price_multiplier()

private_key = wrapper.get_private_key()

to_address = wrapper.get_to_address()

from_token = wrapper.get_from_token()

from_token_amount = wrapper.get_from_token_amount()

to_token = wrapper.get_to_token()

to_token_amount_min = wrapper.get_to_token_amount_min()

w3 = Web3(Web3.HTTPProvider(rpc_url))

from_account = w3.eth.account.from_key(private_key)

nonce = w3.eth.get_transaction_count(from_account.address)

from_token_decimals = (
    w3.eth.contract(address=from_token, abi=ERC20_ABI).functions.decimals().call()
)

to_token_decimals = (
    w3.eth.contract(address=to_token, abi=ERC20_ABI).functions.decimals().call()
)

contract = w3.eth.contract(address=router, abi=UNISWAP_ABI)

print("bot prepared")


def buy(route: list, deadline: int, gas_price: int, idx: int):
    tx = contract.functions.swapExactTokensForTokens(
        int(from_token_amount * 10**from_token_decimals),
        int(to_token_amount_min * 10**to_token_decimals),
        route,
        to_address or from_account.address,
        deadline,
    ).buildTransaction(
        {
            "from": from_account.address,
            "gas": gas_limit,
            "gasPrice": int(gas_price_multiplier * gas_price),
            "nonce": nonce + idx,
        }
    )

    signed_tx = from_account.sign_transaction(tx)

    w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print(f"transaction {idx} sent")


def on_open(ws):
    ws.send(json.dumps({**required_params, **init}))
    ws.send(json.dumps({**required_params, **filter_config}))
    ws.send(json.dumps({**required_params, **watch}))


def on_message(ws, evt):
    data = json.loads(evt)["event"]

    if "contractCall" in data:
        route = [from_token, to_token]
        if data["contractCall"]["methodName"] != "addLiquidity":
            route = [from_token, WBNB, to_token]

        threads = []
        for i in range(buy_times):
            threads.append(
                Thread(
                    target=buy,
                    args=(
                        route,
                        int(data["contractCall"]["params"]["deadline"]),
                        int(data["transaction"]["gasPrice"]),
                        i,
                    ),
                )
            )

        for task in threads:
            task.start()

        for task in threads:
            task.join()

        ws.close()


wsapp = websocket.WebSocketApp(
    "wss://api.blocknative.com/v0", on_open=on_open, on_message=on_message
)
wsapp.run_forever()
