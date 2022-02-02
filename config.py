
walletAddress = "0x0000000000000000000000000000000000000000"                     #Your Wall address From trustwallet or MetaMask or another wallet.
private_key = "0x00000000000000000000000000000000000000000000000000000000000000" #Wallet private_key

spend = "0xe9e7cea3dedca5984780bafc599bd69add087d56"  # WBNB OR BUSD OR USDT OR OTHER contract for buy the token

AmountForSnipe = 1000 # Amount how much you want buy the token in spend.
MinLiquidityAdded = 10  # Set how much minimum liquidity added in pair address that you want to buy. set in WBNB OR OTHER. (eg : 2, 4, 7). 2 mean 2 BNB liquidity added.
MaxSlippage = 25  # Max Slippage or Prince Impact
SellToken = 1   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
Takeprofit = 250 # In percent

transactionRevertTime = 1000 #Limit for make transaction
gasAmount = 500000 #Minimul limit is 210000, more much more better.
gasPrice = 7 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

bscScanAPIKey= "" #Your BSC API Key Get From https://bscscan.com

pancakeSwapRouterAddress = "0x10ED43C718714eb63d5aA57B78B54704E256024E"          #pancakeSwapRouterAddress
pancakeSwapFactoryAddress = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"         #pancakeSwapFactoryAddress
bsc = "https://bsc-dataseed.binance.org/"                                        #BSC JSON-RPC
