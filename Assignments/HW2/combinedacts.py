#!/usr/bin/python3
#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#ALL ACTS COMBINED SCRIPT

import socket

host = "csec380-core.csec.rit.edu"
port = 82
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def getSecureToken():
    s.sendall(b'POST /getSecure HTTP/1.1\r\nHost: csec380-core.csec.rit.edu\r\n\r\n')
    data = s.recv(4096).decode()
    token = data.split(':')[8].strip('\"').strip()
    return token

def act1():
    print("**********************************************ACT1**********************************************")
    s.sendall(b'POST / HTTP/1.1\r\nHost: host\r\n\r\n')
    data = s.recv(4096).decode()
    print (data)
    print("************************************************************************************************\n")

def act2():
    print("**********************************************ACT2**********************************************")
    secureToken = getSecureToken()
    headers = 'POST /getFlag2 HTTP/1.1\r\nHost: host\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n'
    token = "token="+secureToken
    token = token.encode()
    headers = headers.format(content_length = len(token)).encode()
    headers = headers + token
    s.sendall(headers)
    data = s.recv(4096).decode()
    print (data)
    print("************************************************************************************************\n")

def act3():
    print("**********************************************ACT3**********************************************")
    secureToken = getSecureToken()
    headers = 'POST /getFlag3Challenge HTTP/1.1\r\nHost: host\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n'
    token = "token="+secureToken
    token = token.encode()
    headers = headers.format(content_length = len(token)).encode()
    headers = headers + token
    s.sendall(headers)
    data = s.recv(4096).decode()
    captcha = data.split(':')[8].strip('\"').strip()
    solution = eval(captcha)
    headers = 'POST /getFlag3Challenge HTTP/1.1\r\nHost: host\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\n\r\n'
    token = "token="+secureToken+"&solution="+str(solution)
    token = token.encode()
    headers = headers.format(content_length = len(token)).encode()
    headers = headers + token
    s.sendall(headers)
    data = s.recv(4096).decode()
    print (data)
    print("************************************************************************************************\n")

def act4():
    print("**********************************************ACT4**********************************************")
    secureToken = getSecureToken()
    headers = 'POST /createAccount HTTP/1.1\r\nHost: host\r\nAccept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Language: en-US\r\nAccept-Encoding: *\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)\r\nCache-Control: no-cache\r\n\r\n'
    token = "token="+secureToken+"&username=sd9080"
    headers = headers + token
    headers = headers.format(content_length = len(token)).encode()
    s.sendall(headers)
    data = s.recv(4096)
    password = data.decode().split('your password is ')[0].strip()
    password = data.decode().split(' ')[-1].strip('\"').strip()
    password = password.replace('&','%26')
    password = password.replace('=','%3D')
    token = token+"&password="+password
    headers = 'POST /login HTTP/1.1\r\nHost: host\r\nAccept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Language: en-US\r\nAccept-Encoding: *\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {content_length}\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)\r\nCache-Control: no-cache\r\n\r\n'
    headers = headers + token
    headers = headers.format(content_length = len(token)).encode()
    s.sendall(headers)
    data = s.recv(4096) 
    s.close()
    print(data.decode())
    print("************************************************************************************************\n")

def main():
    act1()
    act2()
    act3()
    act4()

if __name__ == '__main__':
    main()