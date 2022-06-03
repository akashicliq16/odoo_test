from asyncore import write
import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'employee'
USER = 'admin'
PASS = '1234'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})


# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)
print("url......",url)
print("uid....",uid)

# create a new note
# args = {
#     # 'color': 8,
#     'name': 'This is another note',
#     # 'create_uid': uid,
# }
# note_id = call(url, "object", "execute", DB, uid, PASS, 'emp_profile.emp_profile', 'create', args)
# print("employee....",note_id)


# read Operation.

# note_read = call(url, "object", "execute", DB, uid, PASS, 'emp_profile.emp_profile', 'read', [6])
# print("employee read....",note_read)

# write/update opreation.

# vals = {
#     'name': 'This is roky** Update',
# }
# note_upd = call(url, "object", "execute", DB, uid, PASS, 'emp_profile.emp_profile', 'write',[6],vals)
# print("employee Update....",note_upd)

# unlink/delete opreation.
note_del = call(url, "object", "execute", DB, uid, PASS, 'emp_profile.emp_profile', 'unlink',[15])
print("employee Delete....",note_del)