import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)


for t in range(10):
    x = {
        "name": "John",
        "age": (30 + t),
        "city": "New York"
        }
    data = json.dumps(x)
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    print('info sent!')
