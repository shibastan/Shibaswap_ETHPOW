from web3 import Web3
import web3 as w3
import json
from uniswap import Uniswap

##### PARAMETERS TO SET #####

# Enter your wallet information (test wallet)
your_addy = Web3.toChecksumAddress('')
pvt_key = ''

# Set maximum slippage (1 = 100%, 0.5 = 50%, 0.001 = 0.1%, etc.)
SLIPPAGE = 0.1

# Address of the token you are selling (currently SHIB)
# Set this to 0x0000000000000000000000000000000000000000 if selling ETH
sell = Web3.toChecksumAddress('0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE')

# Address of the token you are buying (currently ETH)
# Set this to 0x0000000000000000000000000000000000000000 if buying ETH
buy = Web3.toChecksumAddress('0x0000000000000000000000000000000000000000')

# Enter number of token you want to sell
amount_tokens_to_sell = 1000

#############################



# Official ETH POW endpoint
provider_url = 'https://mainnet.ethereumpow.org'
# Web3 provider object
w3 = Web3(Web3.HTTPProvider(provider_url))

# Shibaswap is a UniV2 fork, so use Uniswap client
uni = Uniswap(address=your_addy, private_key=pvt_key, version=2, provider=provider_url)

# Import ERC20 ABI
with open('ERC20_abi.json') as f:
    ERC20_abi = json.load(f)
# Create selling token contract object
selling_token = w3.eth.contract(sell, abi=ERC20_abi)
# Get the number of decimals for the token
if sell == Web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
    sell_decimals = 18
else:
    sell_decimals = selling_token.functions.decimals().call()
# Format selling tokens amount
fomatted_amount_tokens_to_sell = int(amount_tokens_to_sell*(10**(sell_decimals)))

# Create buying token contract object
buying_token = w3.eth.contract(buy, abi=ERC20_abi)
# Get the number of decimals for the token
if buy == Web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
    buy_decimals = 18
else:
    buy_decimals = buying_token.functions.decimals().call()

# Get quote for swap
token_out_quote = uni.get_price_input(sell, buy, fomatted_amount_tokens_to_sell)
print(token_out_quote/(10**(buy_decimals)))

# If okay with the quote them uncomment the below to execute the trade
# receipt = uni.make_trade(sell, buy, fomatted_amount_tokens_to_sell, your_addy, slippage=SLIPPAGE)
# print(receipt)
