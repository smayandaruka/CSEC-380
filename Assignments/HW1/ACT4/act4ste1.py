#Smayan Daruka
#CSEC-380
#Professor Chaim Sanders
#ACT4 Script 1 - act4ste1.py

import requests

def main():
    req = requests.get('https://csec.rit.edu')
    print(req.text)

if __name__ == '__main__':
    main()
