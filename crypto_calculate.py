# enable importing from parent dir
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from crypto_portfolio_me import *
from crypto_portfolio import *

import json, requests, collections



Coin_Data_By_Name =  { } # eg ethereum : { "symb" :  "ETH", "val" : 460, "quantity" :2,  "price": 285, "cap_usd": 200}}
total  = 0;
#-------------------------------
def fiat_code():
    return fiat_curr.name

#-------------------------------
def fiat_price_att():
    # eg "price_eur"
    return "price_" + fiat_code().lower()

#-------------------------------
def is_fiat(name):
    return name == "FIAT"

#-------------------------------
def curr_unit_price( curr_name ):
    url_base = "https://api.coinmarketcap.com/v1/ticker/"
    params = dict(
        convert=fiat_code()
    )

    url = url_base + curr_name

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    if resp.ok is False:
        print("***--Error--*** finding exchange rate for {}, please check https://api.coinmarketcap.com/v1/ticker/".format (curr_name))
        return (curr_name, -1)

    atts = data[0]
    symb = atts['symbol']
    price = atts[fiat_price_att()]
    cap_usd = atts['market_cap_usd']


    ret =  (symb, float(price), cap_usd)
    return ret
#---------------------------------------
def val_exchange(idx_str,  ex_name, ex_info ):
    ex_total = 0

    print("-----------------")
    print (idx_str +   ex_name + "\n" + "-----------------")
    for name, quantity in ex_info.items():

        # short circuit evaluate fiat since its not in rest api (yet)
        if is_fiat(name) :
            symb, price, cap_usd = (fiat_code(), 1, 1)
        else:
            symb, price, cap_usd = curr_unit_price(name)

        # failed to get price .. skip
        if(price < 0):
         continue

        val = price * quantity
        val_str = str(round(val, 2)).rjust(10)
        symb_str = symb.ljust(5)
        quantity_str = str(round(quantity,4)).rjust(8)
        price_str = str(round(price, 2)).rjust(8)

        cap = int(float(cap_usd) / 1000000.0)
        cap_str = ("[" + str(cap) + "]").rjust(7)

        rel_inv = int(float(val / cap) * 100) if (cap > 0) else 1
        rel_inv_str = ("" + str(rel_inv) + "").rjust(7)

        str_out = "{}  {}  {}  {} {}    : ".format(symb_str, cap_str, rel_inv_str,  val_str, fiat_code()) + "{}   coins @ {} {} ".format(quantity_str, price_str, fiat_code())
        print( str_out)
        ex_total = ex_total + val

        # update the Coin_Data (value), or create a new entry in Coin_Data_By_Name if necessary
        Coin_Data = Coin_Data_By_Name.get(name, {})
        Coin_Data["val"] = Coin_Data.get("val", 0)  + val
        Coin_Data["quantity"] = Coin_Data.get("quantity", 0) + quantity
        Coin_Data["price"] = price
        Coin_Data["symb"] = symb
        Coin_Data["cap_usd"] = cap_usd

        Coin_Data_By_Name[name] = Coin_Data



    print("\n" + ex_name + " Total : {} {}".format(round(ex_total,2), fiat_code()))
    print("---------------------------------------- \n")
    return ex_total
#-------------------------------------------------------

def print_curr_to_val():
    print("\n###################################################################################### \n")
    print("            Total Asset Value of each Currency (sorted by value descending)")
    print("\n###################################################################################### \n")

    Val_By_Str_Out = {}
    idx =0
    for name, data in Coin_Data_By_Name.items():
        val     = data["val"]
        val_str = str(int(val)).rjust(10)

        price_str       = str(round(data["price"], 2)).rjust(8)
        symb_str        = data["symb"].ljust(8)
        quantity_str    = str(round(data["quantity"], 3)).rjust(7)
        name_str = ("(" + name + ")") .ljust(15)

        tst = data["cap_usd"]
        cap = int(float(data["cap_usd"]) / 1000000.0)
        cap_str =  ("[" + str(cap) + "]").rjust(7)

        rel_inv = int(float(val/cap) * 100) if(cap > 0) else 1
        rel_inv_str = ("" + str(rel_inv) + "").rjust(7)

        str_out = "{} {} {}   {} {}  {}   :  {}  coins @ {} {}".format(symb_str, name_str, cap_str, rel_inv_str,  val_str, fiat_code(), quantity_str, price_str, fiat_code())
        Val_By_Str_Out[str_out] = val

    OrdDict = collections.OrderedDict(sorted(Val_By_Str_Out.items(), key=lambda t: t[1], reverse=True))
    for str_out, val in OrdDict.items():
        idx = idx + 1
        idx_str =  "({})".format(idx).ljust(8)
        print("{} {}".format(idx_str, str_out))
# --------------------------------------
print("")
print("Explanation of the format of the output:")
print("")
print("'ETH    [35279]       22     7837.89 EUR    :       25   coins @   313.52 EUR '")
print("")
print("  for example, means:")
print("")
print("'You have 7837.89 EUR of ETH'")
print("'ETH has marketCap of 35279 million USD'")
print("'You have 25 coins, each of which is worth 313.52 EUR'")
print("'22' is a measure of the % size of your investment relative to the market cap of the coin. It is calculated from (7837.89/35279)x100")
print("  Higher values mean higher risk, but greater chance of higher profits")
print("")
#curr_unit_price("ethereum")
#curr_unit_price("fct")
print("\n###################################################################################### \n")
print("            Breakdown per Exchange ")
print("\n###################################################################################### \n")




idx_ex =0
for ex_name, ex_info in ex_infos.items():
    idx_ex = idx_ex+1
    idx_str = ("(" + str(idx_ex) + ")" ).ljust(7)
    total = total + val_exchange(idx_str, ex_name, ex_info)
    # print("Type string: {}".format(123))
    # str = quantity + " x " + symb + " " + price +  ",  value = " + val)

print_curr_to_val()

#print ("\nTotal : EUR {}".format(round(total))
profit = total - fiat_invested

print("\n###################################################################################### \n")
print (" Total Profit : {} {}  ({} - {}) ".format(fiat_code(), round(profit, 2), round(total, 2), fiat_invested))
print("\n###################################################################################### \n")




