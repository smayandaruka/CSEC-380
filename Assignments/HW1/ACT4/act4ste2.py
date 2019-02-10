#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#ACT4 Script 2 - act4ste2.py

import urllib.request
import socket
import struct
import sys

def proxy(startIP, endIP):
    startIP = struct.unpack("!L", socket.inet_aton(startIP))[0]
    endIP = struct.unpack("!L", socket.inet_aton(endIP))[0]

    while startIP <= endIP:
        try:
            proxyhandler = urllib.request.ProxyHandler({"http": socket.inet_ntoa(struct.pack("!L", startIP))})
            website = urllib.request.build_opener(proxyhandler)
            webpage = website.open("http://google.com", timeout=2)
            webCode = webpage.getcode()
            if webCode == 200:
                print("IP address: " +
                        socket.inet_ntoa(struct.pack("!I", startIP))  + " is a proxy")
            else:
                pass
        except urllib.request.URLError:
            pass
        startIP = startIP + 1

def main():
    if len(sys.argv) != 3:
        print('Usage: python3 act4ste2.py "START-IP" "END-IP"')
        exit(1)
    startIP = sys.argv[1]
    endIP = sys.argv[2]
    proxy(startIP, endIP)

if __name__ == '__main__':
    main()


