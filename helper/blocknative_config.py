from datetime import datetime
from helper import wrapper, abis

required_params = {
    "timeStamp": datetime.utcnow().isoformat()[:-3] + "Z",
    "dappId": wrapper.get_blocknative_key(),
    "version": "1",
    "blockchain": {"system": "ethereum", "network": "bsc-main"},
}

init = {"categoryCode": "initialize", "eventCode": "checkDappId"}

watch = {
    "categoryCode": "accountAddress",
    "eventCode": "watch",
    "account": {"address": wrapper.get_router()},
}

filter_config = {
    "categoryCode": "configs",
    "eventCode": "put",
    "config": {
        "scope": wrapper.get_router(),
        "filters": [
            {
                "_join": "OR",
                "terms": [
                    {
                        "contractCall.methodName": "addLiquidity",
                        "contractCall.params.tokenA": wrapper.get_to_token(),
                        "status": "pending",
                    },
                    {
                        "contractCall.methodName": "addLiquidity",
                        "contractCall.params.tokenB": wrapper.get_to_token(),
                        "status": "pending",
                    },
                    {
                        "contractCall.methodName": "addLiquidityETH",
                        "contractCall.params.token": wrapper.get_to_token(),
                        "status": "pending",
                    },
                    {
                        "contractCall.methodName": "addLiquidityBNB",
                        "contractCall.params.token": wrapper.get_to_token(),
                        "status": "pending",
                    },
                ],
            }
        ],
        "abi": abis.UNISWAP_ABI,
        "watchAddress": True,
    },
}
