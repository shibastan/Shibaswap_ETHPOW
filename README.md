# Shibaswap_ETHPOW

<b>IANAL but here is a disclaimer:</b><br>
<i>Use this at your own risk - I do not guarantee the accuracy or reliability of this code, nor do I endorse or encourage the use of this software, SHIB or any other currency, exchange platform or transaction facilitated by this code. I'm not responsible for any losses that you might suffer from use of this code.</i><br>
<br>


Python code for swapping tokens on Shibaswap on Proof-of-Work Ethereum
    
1. Install and setup Python (https://realpython.com/installing-python/)


2. Install Python packages <i>web3</i> and <i>uniswap-python</i> by entering the following commands into the command line/terminal. If you have issues with these commands try using "python3" or "py" instead of "python" at the beginning


    - python -m pip install web3
    
    - python -m pip install https://github.com/shibastan/uniswap-python/zipball/master
    
    - Note that I changed a single file (constants.py) in the <i>uniswap-python</i> package to add support for Shibaswap on PoW Ethereum. I have included my version of constants.py in this repo for the reader to review, and I have also made my fork of <i>uniswap-python</i> public so that people can confirm the changes that were made.


3. Download <b>shibaswap.py</b> and <b>ERC20_abi.json</b> from this repo, and save these in the same folder


4. Set parameters in <b>shibaswap.py</b>

    - Include your wallet public key and private key (there are safer ways to pass the private key than in plaintext, but I leave that to the reader)
  
    - Set maximum slippage for the trade (in decimal form)
  
    - Enter token address for the token you are selling and the token you want to buy (check https://www.coingecko.com/ for the Ethereum address, which is the same on PoW as on PoS Mainnet) 
  
    - Enter the amount of tokens you would like to sell


5. Run the code and it will print the expected number of tokens you will get for what you are sending in. If you are okay with this amount, then uncomment the last two lines of <b>shibaswap.py</b> and rerun the code. Happy swapping!

