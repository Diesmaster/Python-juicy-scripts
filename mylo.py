from lib import rpclib
from slickrpc import Proxy
import binascii
import requests
import json
import sys
from lib import bitcoin
from lib import transaction

rpc_user = "changeme"
rpc_password = "alsochangeme"
port =  24708

rpc_connect = rpc_connection = Proxy("http://%s:%s@127.0.0.1:%d"%(rpc_user, rpc_password, port));

list_of_ids = ["22eb1198fc881cd2d6795a7ab97a001e264602d13fb07bc7fda8564cfe89f503"]
list_of_vouts = [1]
address = "RTsRCUy4cJoyTKJfSWcidEwcj7g1Y3gTG5"
amount = 0.001

tx = rpclib.createrawtransaction(rpc_connect, list_of_ids, list_of_vouts, address, amount )

final_res = rpclib.signrawtx(rpc_connect, tx)

decoded = rpclib.decoderawtransaction(rpc_connect, final_res['hex'])

print(decoded)

final_res = final_res['hex']

params = { 'rawtx':final_res }

url = "http://seed.juicydev.coingateways.com:24711/insight-api-komodo/tx/send"

try:
    res = requests.post(url, data=params)
except Exception as e:
    print(e)

print(res.text)
