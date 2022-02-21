<h1>Free pancakeswap sniper bot</h1>
  * Get Your username and offer 50% code: SYBOT50 from: http://pancakesbot.com/

## NOW THE BOT IS POSSIBLE FOR BSC: PANCAKESWAP (DEFAULT)
  YOU CAN USE TO ANY DEFI SAME UNISWAP V2 AND PANCAKESWAP V2, BUT YOU NEED TO CHANGE pairabi, pancakeABI AND pancakeSwapFactoryABI

 
## IMPORTANT NOTES BEFORE RUNNING THE BOT
 CHECK TOKEN YOU WANT TO SNIPER IT NOT SCAM OR HONEYPOT OR SNIPER PROTECTION TOKEN (90% NEW TOKEN CAN BE SCAM)

## NEW UPDATES
1. In this new update you can use BNB instead WBNB. it will make you easier to snipe :)

*What's will you get
To avoid scam, I will invite you to my private repository, aTo avoid scam, I will invite you to my private repository, and you will get whole of code, and any update if I push new update. Please only contact to Telegrame:<code>https://t.me/Sbot_live</code> or <code>eeyang5@gmail.com</code> with subject <b>SY Bot Info</b> for more info. For error or problem questions please open issues in GitHub, don't email me. Maybe I'll slow response on weekend. Thanks!

## Bot future
1. You can snipe new listing token on pancakeswap v2 or any defi like pancakeswap v2 (See how to on above)
2. Sell ALL you token 
3. Sell you token by TakeProfit or Selllimt (Capital is AmountForSnipe)
3. Approve 
4. Check Real price

## How sniper work ?
1. When liquidity added Bot will auto buy and sell when profit more than takeprofit (Please Approve before Sniper)


## HOW TO RUN
1. set up your config.py to with this explanation : 
----------------------------------------------------------
- walletAddress = "0x0000000000000000000000000000000000000000"                     #Your Wall address From trustwallet or another wallet.
- private_key = "x000000000000000000000000000000000000000000000000000000000000000" #Wallet private_key

- spend = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"  # WBNB OR OTHER contract for buy the token

- AmountForSnipe = 0.0024  # Amount how much you want buy the token in WBNB OR OTHER.
- MinLiquidityAdded = 5  # Set how much minimum liquidity added in pair address that you want to buy. set in WBNB OR OTHER. (eg : 2, 4, 7). 2 mean 2 BNB liquidity added.

- SellToken = 0   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
- Takeprofit = 150 # On percent

- transactionRevertTime = 1000 #Limit for make transaction
- gasAmount = 400000 #Minimul limit is 210000, more much more better.
- gasPrice = 5 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

- bscScanAPIKey= "XXXXXXXXXXXXXXXXXXXXXXXXX" #Your BSC API Key Get From bscscan.com

- pancakeSwapRouterAddress = "0x10ED43C718714eb63d5aA57B78B54704E256024E"          #pancakeSwapRouterAddress
- pancakeSwapFactoryAddress = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"         #pancakeSwapFactoryAddress
- bsc = "https://bsc-dataseed.binance.org/"                                        #BSC JSON-RPC
-------------------------------------------------

2. run with <code>SY_Bot.exe</code> include Insert and console windows.

3. Insert Token Contract you want to sniper, than press "Sniper Start" You will see any working on console windows<br>
   <img src="./assets/02.PNG">
   
8. Stop bot with "Stop Running".

## WARNING
The not guarantee make profit every token you snipe, do you research token info before run

## TROUBLESHOOT
* there are some reason if your tx failed :
- you haven't approve your WBNB or Any Token you want to buy or sell
- your gas price are to small
- your GWEI are to small (BSC use 7+ for fast)
