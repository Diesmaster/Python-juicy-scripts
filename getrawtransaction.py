from lib import rpclib
from slickrpc import Proxy
import requests
import json

rpc_user = "changeme"
rpc_password = "alsochangeme"
port =  24708

rpc_connect = rpc_connection = Proxy("http://%s:%s@127.0.0.1:%d"%(rpc_user, rpc_password, port));

address = "RXju6We6DDK9EYhrAVBZVXNAFbA5czw7yK"

url = "http://seed.juicydev.coingateways.com:24711/insight-api-komodo/addrs/RS7y4zjQtcNv7inZowb8M6bH3ytS1moj9A/utxo"

try:
    res = requests.get(url)
except Exception as e:
    print(e)

to_python = json.loads(res.text)

count = 0

list_of_ids = []
list_of_vouts = []
amount = 0


for objects in to_python:
    if (objects['amount'] < 0.01) and count < 10:
        count = count + 1
        easy_typeing2 = [objects['vout']]
        easy_typeing = [objects['txid']]
        list_of_ids.extend(easy_typeing)
        list_of_vouts.extend(easy_typeing2)
        amount = amount + objects['amount']

amount = round(amount, 10)


res = rpclib.createrawtransaction(rpc_connect, list_of_ids, list_of_vouts, address, amount)

print(res)
