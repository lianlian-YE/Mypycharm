from urllib import request
from urllib.request import urlopen

url='http://maoyan.com/board/4'

def get_content(url):
    req=request.Request(url)
    with urlopen(req) as urlObj:
        content=urlObj.read().decode('utf-8')
    print(content)
get_content(url)