# Shibaswap_ETHPOW
Python code for swapping tokens on Shibaswap on Proof-of-Work Ethereum

1. Install and setup Python (https://realpython.com/installing-python/)


2. Install Python packages "web3" and "uniswap-python" by entering the following commands into the command line/terminal

    - python -m pip install web3
    
    - python -m pip install uniswap-python


3. Download/clone this repository


4. Replace constants.py in the uniswap package with constants.py from this repository

    - The folder containing constants.py is called "uniswap" and should be inside a folder called "site-packages". For me, the end of the filepath looks like Python39/Lib/site-packages/uniswap


5. Set parameters in shibaswap.py

    - Include your wallet public key and private key (there are safer ways to pass the private key than in plaintext, but I leave that to the reader)
  
    - Set maximum slippage for the trade (in decimal form)
  
    - Enter token address for the token you are selling and the token you want to buy (check https://www.coingecko.com/ for the Ethereum address, which is the same on PoW as on PoS) 
  
    - Enter the amount of tokens you would like to sell


6. Run code, happy swapping!

