
import requests
from bs4 import BeautifulSoup as bs



#cgv 로그인
'''
while 1:
    member_num = input('CGV 로그인 아이디 입력 : ')
    password = input('비밀 번호 입력 : ')


    driver = webdriver.Chrome('C:\\Users\\F190033\\Downloads\\chromedriver')
    driver.get('https://google.com')


    driver.implicitly_wait(4)
    driver.get('http://www.cgv.co.kr/user/login/?returnURL=http%3a%2f%2fwww.cgv.co.kr%2fdefault.aspx')
    time.sleep(1)
    driver.find_element_by_name('txtUserId').send_keys(member_num)
    time.sleep(1)
    driver.find_element_by_name('txtPassword').send_keys(password)

    driver.find_element_by_xpath('//*[@id="submit"]').click()
    driver.implicitly_wait(3)
    time.sleep(5)


    now_url = driver.current_url
    if now_url == "http://www.cgv.co.kr/default.aspx" :
        break


'''



'''
#----------------------------
#용산 아이파크몰 들어가는거
#----------------------------
driver = webdriver.Chrome('C:\\Users\\F190033\\Downloads\\chromedriver')
driver.get('https://google.com')

driver.get('http://www.cgv.co.kr/default.aspx')
time.sleep(1)
driver.implicitly_wait(3)
time.sleep(1)
driver.find_element_by_css_selector('#gnb_list > li.theaters > a').click()
driver.implicitly_wait(3)
time.sleep(1)
driver.find_element_by_css_selector('#contents > div.sect-common > div > div.sect-city > ul > li.on > div > ul > li:nth-child(23) > a').click()

'''









'''
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

'''


