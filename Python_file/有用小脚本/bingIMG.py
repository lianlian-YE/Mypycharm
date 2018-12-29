import requests
import urllib.request
# URL='https://cn.bing.com/'
URL='http://172.104.78.51:8080'
def getBing(url):
    # header={
    #     'User-Agent':' Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99 Safari / 537.36'
    # }
    rep=urllib.request.urlopen(url)
    response=urllib.request.urlopen(rep)
    html=response.read().encoding('utf8')
    # rep.encoding='utf8'
    
    # print(rep)  #响应对象
    print(html)
getBing(URL)