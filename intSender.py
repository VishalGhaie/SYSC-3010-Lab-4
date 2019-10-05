import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]

n = 10;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

for x in range(n):
    rint = random.randint(1, 10)
    print ("sending integer: " + str(rint))
#   s.sendall(data.encode('utf-8'))
    s.sendto(str(rint).encode('utf-8'), server_address)
