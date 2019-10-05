import socket, sys, time

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

for x in range(10):

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    print ("Received %s bytes from %s %d: " % (len(buf), address,int(buf) ))

s.shutdown(1)

