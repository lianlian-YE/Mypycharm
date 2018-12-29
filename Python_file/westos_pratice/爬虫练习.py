# 作业1： 豆瓣评论分析:
# 1). 获取豆瓣最新上映的所有电影的前10页评论信息；
# 2). 清洗数据；
# 3). 分析每个电影评论信息分析绘制成词云， 保存为png图片，文件名为: 电影名.png;
import requests
from bs4 import BeautifulSoup

url='https://movie.douban.com/cinema/nowplaying/xian/'
def get_reviews(id,pagenum):
    """
    获取指定电影的全部影评
    :return:
    """
    start=(pagenum-1)*20
    
    
def get_url(url):
    """
    获取最新电影列表
    :param url:
    :return:
    """
    responce=requests.get(url)
    content=responce.text
    # print(content)
    soup = BeautifulSoup(content,'html5lib')
    new_playing_list=soup.find_all('li',class_='list-item')
    
    for item in new_playing_list:
        movie_name=item['data_title']
        movie_id=item['id']
        get_reviews(movie_id)