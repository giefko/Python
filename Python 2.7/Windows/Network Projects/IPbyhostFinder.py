#A small educational code to learn how to find from a host the IP address.In this example it find
#your host and your IP address.  
import socket               

s = socket.socket()        
host = socket.getfqdn()

target=raw_input(host)
ip = socket.gethostbyname_ex(target)

print host
print ip
