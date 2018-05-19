__author__ = 'Administor'
# -*- coding: UTF-8 -*-

import urllib
import urllib.request
from bs4 import BeautifulSoup



def temper_crawler(soup):  # 爬取温度
    weather = soup.find_all("p", class_="tem")  # 获得标签
    try:
        weather_l = weather[1].get_text().split('\n')  # 获得标签的内容（get_text)并且去除回车（split)
        weather_h = weather[0].get_text().split('\n')
        weather = weather_l[1] + "~" + weather_h[1]
        return weather
    except:
        return ""


def weather_crawler(soup):
    weather = soup.find_all("p", class_="wea")
    try:
        weather_l = weather[1].get_text().split('\n')
        weather_h = weather[0].get_text().split('\n')
        return weather_l[0]+"转"+ weather_h[0]
    except:
        return ""

def get_description():
    url = "http://www.weather.com.cn/weather1d/101200101.shtml"  # 武汉天气对应的网址
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(req)
    content = response.read().decode('UTF-8')  # 为爬虫设置伪装header
    soup = BeautifulSoup(content, "lxml")
    weather_des = "通哥哥提醒您，今日的天气状况如下：\n" + weather_crawler(soup) +"，" +temper_crawler(soup)+"\n"
    return weather_des
print(get_description())

# temper_crawler(soup)+"\n"+