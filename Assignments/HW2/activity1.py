#!/usr/bin/python3
#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#ACT1 Script - activity1.py

import socket

host = "csec380-core.csec.rit.edu"
port = 82

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'POST / HTTP/1.1\r\nHost: host\r\n\r\n')
    data = s.recv(4096).decode()
    s.close

    print (data)

if __name__ == '__main__':
    main()