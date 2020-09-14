from lib import rpclib
from slickrpc import Proxy
import binascii
import requests
import json
import sys

from lib import bitcoin
from lib import wallet
from lib import commands
from lib import transaction

rpc_user = "changeme"
rpc_password = "alsochangeme"
port =  24708

rpc_connect = rpc_connection = Proxy("http://%s:%s@127.0.0.1:%d"%(rpc_user, rpc_password, port));


privkey = "Uv2jzAFb6UttFYmCWGRyuMxafDHNie15eFe7KYXuvgDzfgWancks"


url = "http://seed.juicydev.coingateways.com:24711/insight-api-komodo/addrs/RS7y4zjQtcNv7inZowb8M6bH3ytS1moj9A/utxo"

maxsize = float(sys.argv[2])
maxcount = int(sys.argv[3])
address = sys.argv[1]

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
    if (objects['amount'] < maxsize) and count < maxcount:
        count = count + 1
        easy_typeing2 = [objects['vout']]
        easy_typeing = [objects['txid']]
        list_of_ids.extend(easy_typeing)
        list_of_vouts.extend(easy_typeing2)
        amount = amount + objects['amount']

amount = round(amount, 10)

#key = rpclib.importprivkey(rpc_connect, privkey)

res = rpclib.createrawtransaction(rpc_connect, list_of_ids, list_of_vouts, address, amount)

test1 = rpclib.decoderawtransaction(rpc_connect, res)

print(test1)

cmd_runner = commands.Commands()

tx = cmd_runner.signtransaction(res, privkey)

final_res = rpclib.signrawtx(rpc_connect, res)

print(tx)

test2 = rpclib.decoderawtransaction(rpc_connect, tx['hex'])
test3 = rpclib.decoderawtransaction(rpc_connect, final_res['hex'])


print(test2)
print(test3)


final_res = final_res['hex']

params = { 'rawtx':final_res }

url = "http://seed.juicydev.coingateways.com:24711/insight-api-komodo/tx/send"

try:
    res = requests.post(url, data=params)
except Exception as e:
    print(e)

print(res.text)
