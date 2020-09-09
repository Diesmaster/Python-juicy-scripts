from lib import rpclib
from slickrpc import Proxy
import requests
import json

rpc_user = "changeme"
rpc_password = "alsochangeme"
port =  24708

rpc_connect = rpc_connection = Proxy("http://%s:%s@127.0.0.1:%d"%(rpc_user, rpc_password, port));

privkey = "Uv2jzAFb6UttFYmCWGRyuMxafDHNie15eFe7KYXuvgDzfgWancks"
tx = "0400008085202f8901c681c0a09a821747c830fb90e46ac66fe190acd92ffa1654103db0dfea5d1d6a000000006b483045022100d445ad36a7e5627c4da20e59af08b9b811417d82474f4eb93a278d0ab51b5a3802201a98d524c736a60c830892ee03e13572c996e37479d8de527bc8aa8cef82e805012102bc84eccf673377b8820f630d4e254c7781914ddcc0315cf7e8261b27e2e711b2ffffffff0240420f00000000001976a914b8bb890b89cd6ef082d363dcb51d8f6ad2e5145188ac9820c211000000001976a914cbeb5be30aaede02316436da368ee57cfcd8187988ac00000000000000000000000000000000000000"


key = rpclib.importprivkey(rpc_connect, privkey)
final_res = rpclib.signrawtx(rpc_connect, tx)

print(final_res)
