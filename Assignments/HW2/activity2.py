#!/usr/bin/python3
#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#ACT2 Script - activity2.py

import socket

host = "csec380-core.csec.rit.edu"
port = 82

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'POST /getSecure HTTP/1.1\r\nHost: csec380-core.csec.rit.edu\r\n\r\n')
    data = s.recv(4096).decode()
    secureToken = data.split(':')[8].strip('\"').strip()

    headers = 'POST /getFlag2 HTTP/1.1\r\nHost: host\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n'
    token = "token="+secureToken
    token = token.encode()
    headers = headers.format(content_length = len(token)).encode()
    headers = headers + token
    s.sendall(headers)
    data = s.recv(4096).decode()
    s.close()

    print(data)

if __name__ == '__main__':
    main()