# Python Sniper Bot

Free lightweight (~300 lines of code) and easy to use liquidity sniper bot based on Web3.py and Blocknative SDK.

Enable you to buy newly listed tokens on DEX in the first place.

## Current Status

Network | Router | Status |
------- | ------ | ------ |
BSC | [PancakeSwap](https://pancakeswap.finance/) | ✅ |
BSC | [Biswap](https://biswap.org/) | ✅ |
BSC | [ApeSwap](https://apeswap.finance/) | ✅ |
Ethereum | [Uniswap](https://app.uniswap.org/) | ⚠️ |
Ethereum | [SushiSwap](https://app.sushi.com/) | ⚠️ |
Polygon | [QuickSwap](https://quickswap.exchange/) | ⚠️ |
Fantom | [SpookySwap](https://spooky.fi/) | ⚠️ |

## Get Started

1. Install [Python3](https://www.python.org/downloads/)
2. Register an account at [Blocknative](https://www.blocknative.com/)
3. Login and check your [Blocknative API key](https://explorer.blocknative.com/account)
4. Follow the corresponding instructions below to get your wallet private key
   - [MetaMask](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-export-an-account-s-private-key)
5. Download and unzip this repository
6. Open [config.py](config.py) and change [line 30](config.py#L30) to
   ```
   TO_TOKEN = "0x55d398326f99059fF775485246999027B3197955"
   ```
7. In terminal, enter following commands to create and enter virtual envrionment
   ```
   python3 -m venv env
   ```
   Linux or macOS
   ```
   source env/bin/activate
   ```
   Windows
   ```
   env\Scripts\activate.bat
   ```
8. Install dependencies in virtual environment
   ```
   pip install -r requirements.txt
   ```
9. Set environment varibale in virtual environment
   
   Linux or macOS
   ```
   export BLOCKNATIVE_KEY=<your Blocknative API key>
   export PRIVATE_KEY=<your wallet private key>
   ```
   Windows
   ```
   set BLOCKNATIVE_KEY=<your Blocknative API key>
   set PRIVATE_KEY=<your wallet private key>
   ```
10. In terminal, enter the following command
    ```
    python3 main.py
    ```
11. Now, when someone add liquidity with USDT on BSC, you will spend 0.001 BNB to buy USDT with path \[BNB, USDT paired token, USDT\]