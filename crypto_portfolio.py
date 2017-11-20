from crypto_fiats import *

############################################################################
#---------------------------------------------------------------------------
#--------------------- User Settings ---------------------------------------
#---------------------------------------------------------------------------
############################################################################

# Modify this file to match your portfolio, and reference (fiat) currency.
# You can group your cryptocurriencies per exchange (as below) or put all in one group with any arbitrary name.


# (1) which fiat currency you want coin values calculated in (choose from list in crypto_fiats.py)
fiat_curr = Fiat.EUR

# (2) specify how much of this fiat currency you invested (will be used to calculate profit/loss)
fiat_invested  = 40000
# (3) specify how much of each cryptocurrency you bought (grouped by exchange)
# Exchange name is not used in calculation, just for display purposes
# See https://coinmarketcap.com/api/ for list of currency possible values
# Use value "FIAT" if you want to include your non crypto currency as specified in (1)
ex_infos = {

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
    },


    "Coss": {
        "coss": 2000,
        "civic": 1000,
        "eos": 500,
        "lisk": 1000,
        "ethereum": 7,
    },

    "Binance" : {
        "binance-coin"  : 500,
        "ethereum"      : 12,
        "eos"           : 10000,
        "omisego"       : 500,
     },

    "Bittrex": {
        "factom": 10,
        "ethereum": 4,
        "civic": 200,
    },



}
############################################################################
#---------------------------------------------------------------------------
#--------------------- End of User Settings --------------------------------
#---------------------------------------------------------------------------
############################################################################
