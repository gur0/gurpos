import socket
import itertools

ip = sys.argv[1]
port = int(sys.argv[2])

soc = socket.socket()
soc.connect((ip, port))

count = 0
# int_list = [chr(x) for x in range(48, 58)]
chr_list = [chr(x) for x in range(97, 123)] + [chr(x) for x in range(48, 58)]

for i in range(1, 5):
    count += 1
    if count >= 1000000:
        print("Too many attempts")
        soc.close()
        break
    my_iter = itertools.combinations(chr_list, i)
    while True:
        try:
            msg = ''.join(next(my_iter))
            soc.send(msg.encode())
            res = soc.recv(1024)
            res_str = res.decode()
            if res_str == "Connection success!":
                print(msg)
                soc.close()
                break
            elif res_str == "Wrong password!":
                continue
        except:
            break
