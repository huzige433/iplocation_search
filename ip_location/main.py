#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-11 23:44:26
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @Link    : https://github.com/KellyHwong/ip138
# @Version : $0.0.0$
import random
import time

import requests
from lxml import etree


def ip138(ip):
    '''
    ip138 IP geometry infomation API
    :@param ip (str): query ip address (str)
    :@return (dict):
    '''
    proxy=getip()
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"%random.randint(1000,9999)
    }
    proxies={
        'http':'http://%s' % proxy
    }
    url = "https://site.ip138.com/%s/" % ip
    query_html = requests.get(url,headers=HEADERS,proxies=proxies,timeout=3000).content
    query_html = query_html.decode("utf8")
    html=etree.HTML(query_html)
    try:
     returntxt=html.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/h3")[0].text
     return returntxt
    except Exception as ex:
        Globelip.proxyglobal=None
        return ip138(ip)

def start(file):
    with open(file , 'r' , encoding='UTF-8') as f :
        jsontxyt = f.readlines()
        for ip in jsontxyt :
            ip=ip.strip()
            txt=ip+" "+ip138(ip)+'\n'
            print(txt,"查询ip%s"%Globelip.proxyglobal)
            with open('ip_location.txt' , 'a+' , encoding="utf8") as f :
                f.write(txt)

def getip():

    if not  Globelip.proxyglobal or "请求太频繁，请1秒后访问" in Globelip.proxyglobal:
        time.sleep(10)
        url="http://119.23.215.249:8081/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=101&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=&usertype=2"
        html=requests.get(url).content
        html=html.decode("utf8")
        print("获取代理%s"%html)
        Globelip.proxyglobal=html
        return Globelip.proxyglobal
    else:

        return Globelip.proxyglobal

class Globelip:
    proxyglobal=None

if __name__=="__main__":
    import sys
    filename = sys.argv[1]
    # filename=r"C:\Users\41427\Desktop\iplocation\ip_20221214.txt"
    start(filename)



