import os
import sys
import re
import time
import random
import requests as ModcaTheLost

class modca:
 def __init__(self):
  url = "https://free-proxy-list.net/"
  proxies = []
  os.system("clear")
  proxy1 = ModcaTheLost.get(url).text
  proxy2 = re.findall(r"<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+?)</td>", proxy1)
  for x in proxy2:
   proxies.append(":".join(x))
  try:tanya_total = int(input("Kaç Tane Proxy Çekilsin -> "))
  except:tanya_total = 1
  print("Bekle")
  time.sleep(3) 
  for total in range(tanya_total):
   total +=1
   proxy = random.choice(proxies)
   print("proxy %s -> %s"%(total, proxy))
  ask = input("Devam Edelim Mi? Y/n ")
  if ask in ["Y", "y"]:
   modca()
  else:
   exit("Görüşmek üzere !!")
try:
 modca()
except Exception as e:
 exit(str(e))