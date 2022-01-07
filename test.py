#提交一次
import requests
from requests.auth import HTTPBasicAuth
import time
from bs4 import BeautifulSoup

cook={'_gcl_au':"1.1.662794399.1637505532",
         '_ga':'GA1.2.2021433332.1637505533',
         'cw_conversation':'eyJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfaWQiOiJhNDI1Y2Y5ZS1hZDE3LTQ0ZWMtYTNkOS03NGUwNzc3ODkxZTEiLCJpbmJveF9pZCI6M30.7FzWXQ_Fk53bk7vIbMiH1yZ7dgnAWffqLIgnyNMCocA',
         'PHPSESSID':'88c8a7da831c208c1468904d2f7fd968',
         'uid':'1897',
         'email':'1109479588%40qq.com',
         'key':'49745a59aed0e6302c53765725f7242f277b6475f83b8',
         'ip':'7c0e32560d1fe81d9f98889e17393f22',
         'expire_in':'1641800511',
         '_gid':'GA1.2.492933576.1641343170'
     }
header={'Host': 'lichen.mutualism.zone',
'Cache-Control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://lichen.mutualism.zone/user',
'Accept-Language': "en-US,en;q=0.9"}

key="SCT110020T1xPaSPaJ0iZKD2BpPbK8Gi7x"

post_url="https://lichen.mutualism.zone/user/checkin"
get_url="https://lichen.mutualism.zone/user"

r=requests.get(get_url,headers=header,cookies=cook)

print(r.text)
