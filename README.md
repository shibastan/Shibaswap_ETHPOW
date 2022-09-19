# Shibaswap_ETHPOW
Python code for swapping tokens on Shibaswap on Proof-of-Work Ethereum

1. Install and setup Python (https://realpython.com/installing-python/)


2. Install Python packages "web3" and "uniswap-python" by entering the following commands into the command line/terminal. If you have issues with these commands try using "python3" or "py" instead of "python" at the beginning


    - python -m pip install web3
    
    - python -m pip install https://github.com/shibastan/uniswap-python/zipball/master


3. Download <b>shibaswap.py</b> and <b>ERC20_abi.json</b> from this Github, and save these in the same folder


4. Set parameters in <b>shibaswap.py</b>

    - Include your wallet public key and private key (there are safer ways to pass the private key than in plaintext, but I leave that to the reader)
  
    - Set maximum slippage for the trade (in decimal form)
  
    - Enter token address for the token you are selling and the token you want to buy (check https://www.coingecko.com/ for the Ethereum address, which is the same on PoW as on PoS) 
  
    - Enter the amount of tokens you would like to sell


5. Run code, happy swapping!

