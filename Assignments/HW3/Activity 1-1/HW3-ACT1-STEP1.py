#!/usr/bin/python3
#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#HW3 - ACT 1 - STEP 1

import csv
import requests
import socket
import ssl
import time
from bs4 import BeautifulSoup

host = "rit.edu"
port = 443
ttl = 2
file = open('csec-courses.csv', 'w')
s = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
s.connect((host, port))

def getdata():
    course = ''
    courses = []
    timer = time.time()
    while timer != 0:
        if (courses != 0) and (time.time() - timer > ttl):
            break
        course = s.recv(4096).decode()
        if course:
            courses.append(course)
            timer = time.time()
    courses = "".join(courses)
    return courses

def act1():
    print("**********************************************ACT 1 - STEP 1**********************************************")
    s.sendall(b'GET /programs/computing-security-bs HTTP/1.1\r\nHost: www.rit.edu\r\n\r\n')
    courses = getdata()
    soup = BeautifulSoup(courses, "html.parser")
    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        if not td or td[0].attrs or td[0].text == u"\xa0":
            continue
        csv.writer(file).writerow([(td[0].text.strip()), (td[1].text.strip())])

def main():
    act1()    
    s.close()

if __name__ == '__main__':
    main()