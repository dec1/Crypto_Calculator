# Crypto Calculator
Quickly and easily calculate the current gain/loss of your Cryprocurrency Portfolio using real time data from  [CoinMarketCap](https://coinmarketcap.com/api/)

*If you have bought several cryptocurrencies it can be troublesome keeping track of how much your investment is worth (in fiat) at any given time. This is especially true (and interesting) considering how fast the exchange rates are changing. If your investment is spread out across several exchanges this exacerbates this problem. This script automates the process, and can present the results in your choice of several fiat currencies EUR, USD, GBP etc.*

## Prerequisites
* Python 3

## Usage

* Make sure you have the necessary python packages installed
```python 
pip3 install requests
```

* Specify what currencies you have bought by editing the file
 **[crypto_portfolio.py](crypto_portfolio.py)**  
   (*For a complete list of possible currencies see [here](https://api.coinmarketcap.com/v1/ticker/)*)


```python 
...
    "Kraken": {

        "ripple"    : 200,
        "monero"    : 20,
        "FIAT"      : 1200,
        "ethereum"  : 25,
        "augur"     : 50.5,
    },



    "KuCoin": {
        "kucoin-shares": 100,
        "neblio": 500,
        "ethereum": 5,
    }
...

```
* Run the script
```python 
python3 crypto_calculator.py
```

## Sample output

```python 
###################################################################################### 

            Breakdown per Exchange 

###################################################################################### 

#-----------------
(1)    Kraken
#-----------------
XRP     [9401]        0       41.47 EUR    :      200   coins @     0.21 EUR 
XMR     [2148]      110     2380.07 EUR    :       20   coins @    119.0 EUR 
EUR        [0]        1        1200 EUR    :     1200   coins @        1 EUR 
ETH    [35284]       22     7839.02 EUR    :       25   coins @   313.56 EUR 
REP      [229]      392      898.98 EUR    :     50.5   coins @     17.8 EUR 

Kraken Total : 12359.53 EUR
#---------------------------------------- 

#-----------------
(2)    KuCoin
#-----------------
KCS       [58]       94       54.84 EUR    :      100   coins @     0.55 EUR 
NEBL      [39]     3454     1347.07 EUR    :      500   coins @     2.69 EUR 
ETH    [35284]        4      1567.8 EUR    :        5   coins @   313.56 EUR 

KuCoin Total : 2969.71 EUR
#---------------------------------------- 

#-----------------
(3)    Coss
#-----------------
COSS       [5]     2205      110.28 EUR    :     2000   coins @     0.06 EUR 
CVC      [120]      249      299.54 EUR    :     1000   coins @      0.3 EUR 
EOS      [993]       87      865.57 EUR    :      500   coins @     1.73 EUR 
LSK     [1148]      740      8497.6 EUR    :     1000   coins @      8.5 EUR 
ETH    [35284]        6     2194.93 EUR    :        7   coins @   313.56 EUR 

Coss Total : 11967.91 EUR
#---------------------------------------- 

#-----------------
(4)    Binance
#----------------
BNB      [161]      430      693.81 EUR    :      500   coins @     1.39 EUR 
ETH    [35284]       10     3762.73 EUR    :       12   coins @   313.56 EUR 
EOS      [993]     1743    17311.48 EUR    :    10000   coins @     1.73 EUR 
OMG      [832]      417     3473.31 EUR    :      500   coins @     6.95 EUR 

Binance Total : 25241.33 EUR
#---------------------------------------- 

#-----------------
(5)    Bittrex
#-----------------
FCT      [171]       97      166.98 EUR    :       10   coins @     16.7 EUR 
ETH    [35284]        3     1254.24 EUR    :        4   coins @   313.56 EUR 
CVC      [120]       49       59.91 EUR    :      200   coins @      0.3 EUR 

Bittrex Total : 1481.14 EUR
#---------------------------------------- 


###################################################################################### 

            Total Asset Value of each Currency (sorted by value descending)

###################################################################################### 

(1)      EOS      (eos)             [993]      1830      18177  EUR   :    10500  coins @     1.73 EUR
(2)      ETH      (ethereum)      [35284]        47      16618  EUR   :       53  coins @   313.56 EUR
(3)      LSK      (lisk)           [1148]       740       8497  EUR   :     1000  coins @      8.5 EUR
(4)      OMG      (omisego)         [832]       417       3473  EUR   :      500  coins @     6.95 EUR
(5)      XMR      (monero)         [2148]       110       2380  EUR   :       20  coins @    119.0 EUR
(6)      NEBL     (neblio)           [39]      3454       1347  EUR   :      500  coins @     2.69 EUR
(7)      EUR      (FIAT)              [0]         1       1200  EUR   :     1200  coins @        1 EUR
(8)      REP      (augur)           [229]       392        898  EUR   :     50.5  coins @     17.8 EUR
(9)      BNB      (binance-coin)    [161]       430        693  EUR   :      500  coins @     1.39 EUR
(10)     CVC      (civic)           [120]       299        359  EUR   :     1200  coins @      0.3 EUR
(11)     FCT      (factom)          [171]        97        166  EUR   :       10  coins @     16.7 EUR
(12)     COSS     (coss)              [5]      2205        110  EUR   :     2000  coins @     0.06 EUR
(13)     KCS      (kucoin-shares)    [58]        94         54  EUR   :      100  coins @     0.55 EUR
(14)     XRP      (ripple)         [9401]         0         41  EUR   :      200  coins @     0.21 EUR

###################################################################################### 

 Total Profit : EUR 14019.62  (54019.62 - 40000) 

###################################################################################### 

```

## Explanation of the format of the output
``` 
'ETH    [35279]       22     7837.89 EUR    :       25   coins @   313.52 EUR '

  for example, means:

'You have 7837.89 EUR of ETH'
'ETH has marketCap of 35279 million USD'
'You have 25 coins, each of which is worth 313.52 EUR'
'22' is a measure of the % size of your investment relative to the market cap of the coin. It is calculated from (7837.89/35279)x100
  Higher values mean higher risk, but greater chance of higher profits
```
