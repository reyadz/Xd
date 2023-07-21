from os import path
import os,base64,zlib,pip,urllib,time,sys
import os
import time
import requests

import subprocess
import os
try:
	os.system('pip uninstall -y requests && pip install requests')
	exit('python drx.py')
#------------------[ MACHINE-SUPPORT ]---------------#

def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
#------------------[ APPROVAL SYSTEM ]-------------------#

def approval():
  time.sleep(1)
  uuid = str(os.geteuid())+"DAD"+str(os.geteuid())
  id = "RXS-"+"".join(uuid)
  os.system('clear')
  banner()
  animation("\033[1;37m [\u001b[36m𝜩\033[1;37m] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
  print("\033[1;37m [\u001b[36m𝜩\033[1;37m] YOUR KEY :\u001b[36m "+id);time.sleep(0.1)
  print ("""\x1b[92m══════════════════════════════════════════════\x1b[97m""")
  try:
    httpCaht = requests.get("https://github.com/reyadz/PAID-RXS/blob/main/rxs_pfgaid.txt").text
    if id in httpCaht:
      animation("\033[1;97m [\u001b[36m❯\033[1;37m] YOUR KEY HAS BEEN APPROVED !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      animation("\x1b[1;97m [\u001b[36m❯\033[1;37m] SORRY YOUR KEY HAS NOT BEEN APPROVED ");
      time.sleep(0.1)
      animation("\033[1;37m [\u001b[36m1\033[1;37m] CONTACT ADMIN REYAD   \033[1;37m")
      animation("\033[1;37m [\u001b[36m2\033[1;37m] CONTACT ADMIN TAHOSIN   \033[1;37m")
      ok = input(' [\u001b[36m❯\033[1;37m] CHOOSE ADMIN TO CONTACT ')
      if ok =='2':
      	os.system('xdg-open https://wa.me/+8801989861704?text=Assalamuwalaikum%20Sir,%20I%20Want%20To%20Buy%20Your%20RXS%20Paid%20Tool.%20My%20Key:%20'+id)
      if ok =='1':
      	os.system('xdg-open https://www.facebook.com/reyadbross')
      time.sleep(1)
      approval()
  except: 
     exit() 
approval()
time.sleep(1.5)
print('[\033[1;36m√\033[1;37m] Updating Tool ! ')
time.sleep(1.5)
os.system("clear")
print('[\033[1;36m√\033[1;37m] Tool Update Done')
time.sleep(1.5)
print('[\033[1;36m√\033[1;37m] Now You Can Enjoy Tool (^,^) ')
time.sleep(1.5)
os.system("clear")
print("""
\033[1;36m███    ██ ███████ ██   ██  █████  ██      
\033[1;36m████   ██ ██      ██   ██ ██   ██ ██      
\033[1;36m██ ██  ██ █████   ███████ ███████ ██      
\033[1;36m██  ██ ██ ██      ██   ██ ██   ██ ██      
\033[1;36m██   ████ ███████ ██   ██ ██   ██ ███████ 
\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m
\033[1;36m[😈] DEVELOPER : NEHAL KHAN   
\033[1;36m[😈️] GITHUB    : Nehal901   
\033[1;36m[😈] TOOL NAME : METHOD CAPTURE
\033[1;36m[😈] TOOL TYPE : PAID 
\033[1;36m[😈] VERSION   : 0.1
\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m""")
print("\033[1;36mYOUR KEY : A4HT8GSTR85B5ETY5D")
print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
print("[+] CONTACT ADMIN TO GET APPROVAL")
input('[+] PRESS ENTER TO BUY APPROVAL')
os.system("xdg-open https://wa.me/+8801775174361")
print("\033[1;32m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━━═━━━═━━═━\033[1;37m")
