# Crypto Calculator
Quickly and easily calculate the current gain/loss of your Cryprocurrency Portfolio using real time data from  [CoinMarketCap](https://coinmarketcap.com/api/)

*If you have bought several cryptocurrencies it can be troublesome keeping track of how much your investment is worth (in fiat) at any given time. This is especially true (and interesting) considering how fast the exchange rates are changing. If your investment is spread out across several exchanges this exacerbates this problem. This script automates the proces, and can present the results in your choice of several fiat currencies EUR, USD, GBP etc.*

## Prerequisites
* Python 3

## Usage

* Make sure you have the necessary python packages installed
```python 
pip3 install requests
```

* Specify what currencies you have bought by editing the file
 **crypto_portfolio.py**  
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

-----------------
(1)    Kraken
-----------------
XRP         40.32 EUR    :      200   coins @      0.2 EUR 
XMR       2285.28 EUR    :       20   coins @   114.26 EUR 
EUR          1200 EUR    :     1200   coins @        1 EUR 
ETH       7628.19 EUR    :       25   coins @   305.13 EUR 
REP        865.38 EUR    :     50.5   coins @    17.14 EUR 

Kraken Total : 12019.17 EUR
---------------------------------------- 

-----------------
(2)    KuCoin
-----------------
KCS         55.48 EUR    :      100   coins @     0.55 EUR 
NEBL      1321.98 EUR    :      500   coins @     2.64 EUR 
ETH       1525.64 EUR    :        5   coins @   305.13 EUR 

KuCoin Total : 2903.09 EUR
---------------------------------------- 

-----------------
(3)    Coss
-----------------
COSS       116.86 EUR    :     2000   coins @     0.06 EUR 
CVC        304.04 EUR    :     1000   coins @      0.3 EUR 
EOS        800.66 EUR    :      500   coins @      1.6 EUR 
LSK       8507.68 EUR    :     1000   coins @     8.51 EUR 
ETH       2135.89 EUR    :        7   coins @   305.13 EUR 

Coss Total : 11865.13 EUR
---------------------------------------- 

-----------------
(4)    Binance
-----------------
BNB        673.91 EUR    :      500   coins @     1.35 EUR 
ETH       3661.53 EUR    :       12   coins @   305.13 EUR 
EOS      16013.22 EUR    :    10000   coins @      1.6 EUR 
OMG       3390.97 EUR    :      500   coins @     6.78 EUR 

Binance Total : 23739.63 EUR
---------------------------------------- 

-----------------
(5)    Bittrex
-----------------
FCT         162.9 EUR    :       10   coins @    16.29 EUR 
ETH       1220.51 EUR    :        4   coins @   305.13 EUR 
CVC         60.81 EUR    :      200   coins @      0.3 EUR 

Bittrex Total : 1444.21 EUR
---------------------------------------- 


###################################################################################### 

            Total Asset Value of each Currency (sorted by value descending)

###################################################################################### 

(1)      EOS      (eos)             16813.88  EUR   :    10500  coins @      1.6 EUR
(2)      ETH      (ethereum)        16171.75  EUR   :       53  coins @   305.13 EUR
(3)      LSK      (lisk)             8507.68  EUR   :     1000  coins @     8.51 EUR
(4)      OMG      (omisego)          3390.97  EUR   :      500  coins @     6.78 EUR
(5)      XMR      (monero)           2285.28  EUR   :       20  coins @   114.26 EUR
(6)      NEBL     (neblio)           1321.98  EUR   :      500  coins @     2.64 EUR
(7)      EUR      (FIAT)                1200  EUR   :     1200  coins @        1 EUR
(8)      REP      (augur)             865.38  EUR   :     50.5  coins @    17.14 EUR
(9)      BNB      (binance-coin)      673.91  EUR   :      500  coins @     1.35 EUR
(10)     CVC      (civic)             364.85  EUR   :     1200  coins @      0.3 EUR
(11)     FCT      (factom)             162.9  EUR   :       10  coins @    16.29 EUR
(12)     COSS     (coss)              116.86  EUR   :     2000  coins @     0.06 EUR
(13)     KCS      (kucoin-shares)      55.48  EUR   :      100  coins @     0.55 EUR
(14)     XRP      (ripple)             40.32  EUR   :      200  coins @      0.2 EUR

###################################################################################### 

 Total Profit : EUR 11971.23  (51971.23 - 40000) 

###################################################################################### 
 
```
