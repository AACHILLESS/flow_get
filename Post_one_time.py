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
         '_gid':'GA1.2.492933576.1641343170'}

key="SCT110020T1xPaSPaJ0iZKD2BpPbK8Gi7x"

post_url="https://lichen.mutualism.zone/user/checkin"
get_url="https://lichen.mutualism.zone/user"


def check_flows(url,cook,key):
    print("enter check flows!")
    r=requests.get(get_url,cookies=cook)
    print("get ok!")
    r.encoding = r.apparent_encoding
    s=BeautifulSoup(r.text,features="html.parser")
    print(s)
    infma=s.find_all("div",class_="card-inner margin-bottom-no")
    print(infma)
    print('find is OK')
    for i in infma.children:
        if i.string is None:
            continue
        if "剩余量" in i.string:
            print("enter flow ftqq send!")
            requests.get("https://sc.ftqq.com//{}.send?text={}&desp={}".format(key,"check_flow",i.string))
    print("send ok!")

def get_day_flows(post_url,get_url,cook,key):
    
    print("enter post flow!")
    
    resp=requests.post(post_url,cookies=cook)
    check_flows(get_url,cook,key)
    
    print("enter post flow send!")
    
    if eval(resp.text)['msg'] != '您似乎已经续命过了...':
        requests.get("https://sc.ftqq.com//{}.send?text={}&desp={}".format(key,"post_res",eval(resp.text)['msg']))
    else:
        requests.get("https://sc.ftqq.com//{}.send?text={}&desp={}".format(key,"post_res",'您似乎已经续命过了...'))
        
def main():
    for i in range(100):
        print(i)
        try:
            get_day_flows(post_url,get_url,cook,key)
            return 0
        except:
            print("error")
            continue
if __name__=="__main__":
    get_day_flows(post_url,get_url,cook,key)
