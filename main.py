from threading import Timer
import requests
import re
import itchat


def get(url):
    ua={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    response = requests.get(url,headers = ua)
    if response.status_code == 200:
        response.encoding ='utf-8'
        return response.text
    return None
def parse(html):
    pattern = re.compile('<div class="wea_weather clearfix">[\s\S]*?<em>([\s\S]*?)</em>[\s\S]*?<b>([\s\S]*?)</b>')
    item = re.findall(pattern,html)
    return item[0]
def parse2(html):
    pattern = re.compile('<div class="wea_about clearfix">[\s\S]*?<span>([\s\S]*?)</span>[\s\S]*?<em>([\s\S]*?)</em>')
    item = re.findall(pattern,html)
    return item[0]
def parse3(html):
    pattern = re.compile('<div class="wea_tips clearfix">[\s\S]*?<span>([\s\S]*?)</span>[\s\S]*?<em>([\s\S]*?)</em>')
    item = re.findall(pattern,html)
    return item[0]

def send(data):
    itchat.auto_login()
    name = itchat.search_friends(remarkName='pink')[0]['UserName']
    message = data[1]+'，气温'+data[0]+'度,'+dats[0]+','+dats[1]+','+datd[0]+':'+datd[1]
    itchat.send_msg(msg='新郑市今天天气: '+message,toUserName=name)
    
    
    
if __name__=='__main__':
    url = 'https://tianqi.moji.com/weather/china/henan/xinzheng'
    html = get(url)
    data = parse(html)
    dats = parse2(html)
    datd = parse3(html)
    print(data)
    print(dats)
    print(datd)
    send(data)
    
    
   
