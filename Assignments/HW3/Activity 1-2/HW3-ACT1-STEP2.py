#!/usr/bin/python3
#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#HW3 - ACT 1 - STEP 2

import requests
import socket
import ssl
import threading 
import time
from bs4 import BeautifulSoup

host = "rit.edu"
port = 443
ttl = 2
s = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
s.connect((host, port))

def getdata():
    picture = ''
    pictures = []
    timer = time.time()
    while timer != 0:
        if (pictures != 0) and (time.time() - timer > ttl):
            break
        picture = s.recv(4096).decode()
        if picture:
            pictures.append(picture)
            timer = time.time()
    pictures = "".join(pictures)
    return pictures

def act1():
    print("**********************************************ACT 1 - STEP 2**********************************************")
    s.sendall(b'GET /gccis/computingsecurity/people HTTP/1.1\r\nHost: www.rit.edu\r\n\r\n')
    pictures = getdata()
    soup = BeautifulSoup(pictures, "html.parser")
    for tr in soup.find_all("img"):
        f = open("trial", 'w')
        f.write(pictures)
        f.close()
        
def main():
    thread = threading.Thread(target=act1, args=())
    act1()    
    s.close()

if __name__ == '__main__':
    main()