import argparse
from eospy.cleos import Cleos
import time
import requests


# args
parser = argparse.ArgumentParser(description='Push token price to delphioracle')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--key-permission','-k', type=str, action='store', required=True, dest='key_permission')
parser.add_argument('--broadcast','-b', action='store_true', dest='broadcast')
args = parser.parse_args()

# connect up
ce = Cleos(args.url)

def get_coinbase() :
    # https://developers.coinbase.com/docs/wallet/guides/price-data
    # {"data":{"base":"BTC","currency":"USD","amount":"6444.61"}}
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    r = requests.get(url)
    r.raise_for_status()
    return float(r.json()['data']['amount'])

def get_bitfinex(btc_usd) :
    # https://docs.bitfinex.com/v2/reference#rest-public-tickers
    url = 'https://api.bitfinex.com/v2/ticker/tEOSBTC'
    r = requests.get(url)
    r.raise_for_status()
    # get last price
    return float(r.json()[6]) * btc_usd

def get_binance(btc_usd) :
    # docs: https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
    # {"symbol":"EOSBTC","price":"0.00082840"}

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=EOSBTC'
    # get EOS -> BTC
    r = requests.get(url)
    r.raise_for_status()
    eos_btc = float(r.json()['price'])
    return (eos_btc * btc_usd)

def get_idax(btc_usd) :
    # docs : https://github.com/idax-exchange/idax-official-api-docs/blob/master/open-api_en.md
    #{
    #    "code":10000,
    #    "msg":"request success",
    #    "timestamp":1536320917805, //server time for returned data
    #    "ticker":[
    #    {
    #        "pair":"ETH_BTC", //pair
    #        "open":"0.03528700", //open price
    #        "high":"0.03587400", //high price
    #        "low":"0.03389300",//low price
    #        "last":"0.03428700",//last price
    #        "vol":"18484.75200000"//volume(in the last 24hours sliding window)
    #    }]
    #}
    base_url = 'https://openapi.idax.mn/api/v2/ticker?pair={}'
    eosbtc_symbol = 'EOS_BTC'
    # get EOS -> BTC
    r = requests.get(base_url.format(eosbtc_symbol))
    r.raise_for_status()
    return float(r.json()['ticker'][0]['last']) * btc_usd

while(True) :
    # get btc_usd price
    btc_usd = get_coinbase()
    # get 
    bitfinex = get_bitfinex(btc_usd)
    print("bitfinex: {}".format( bitfinex))

    binance = get_binance(btc_usd)
    print("binance: {}".format(binance))

    idax = get_idax(btc_usd)
    print("idax: {}".format(idax))
    avg_price = round((bitfinex + binance + idax) / 3, 2)*10000
    print(int(avg_price))
    # create transaction
    account = 'eosnewyorkio'
    permission = 'delphioracle'
    data = ce.abi_json_to_bin('delphioracle', 'write',{'owner':account, 'value': avg_price})
    trx = {"actions":
    [{
        "account":'delphioracle',
        "name":"write",
        "authorization":[
            {
                "actor":account,
                "permission": permission
            }],
        "data":data['binargs']}
    ]}
    # transaction
    try :
        resp = ce.push_transaction(trx, args.key_permission, broadcast=args.broadcast)
        print(resp)
    except ValueError as ex:
        print(ex)
    # sleep for 60 seconds
    time.sleep(60)
