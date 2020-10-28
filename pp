
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20201030&screencodes=&screenratingcode=&regioncode="
html = requests.get(url)
soup = bs(html.text , "html.parser")
title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one('a > strong').text.strip()) #a태그 걸어 오는거

imax = soup.select_one('span.imax')
if(imax):
    imax = imax.find_parent('div' , class_= 'col-times')
    title = imax.select_one('div.info-movie> a > strong').text.strip()
    print(title + "IMAX가 열렸습니다.")
else :
    print("IMAX가 안열렸습니다." )




