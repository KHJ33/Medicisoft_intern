import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


URL = 'http://www.demoday.co.kr/companies/rank/weekly'
html = requests.get(URL)

soup = BeautifulSoup(html.text,'html.parser')

content = soup.find(class_='contents-list')
content_li = content.find_all('li')

print(len(content_li))

df_input = []
col = ['회사', '서비스구분', '종류', '상세내용', '기본 포맷']
for web in content_li:
    b = []
    a = web.find('a')
    # print(a['href'])
    url = 'http://www.demoday.co.kr' + a['href']
    print(url)
    driver = webdriver.Chrome('C:/Users/mdc_int_94/Desktop/chromedriver.exe')

    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.select_one('#company_container > div > #mid_wrap > #company_basic_info > #info')
    name = body.select_one('#info > h1').text
    coment = body.select_one('#info > p').text  # 서비스 구분
    details = body.select_one('#company_details > li:nth-child(4) > span.value').text  # 카테고리
    # 사업분야 = body.select_one('#company_details > li:nth-child(5) > span.value').text

    try:
        body = soup.select_one('#company_container > div > #mid_wrap > #company_basic_info > #info')
        name = body.select_one('#info > h1').text
        coment = body.select_one('#info > p').text  # 서비스 구분
        details = body.select_one('#company_details > li:nth-child(4) > span.value').text  # 카테고리
        소개 = soup.find(class_='service-desc').text
        #print(name, coment, details, 사업분야)
        b.append(name)
        b.append(coment)
        b.append(details)
        b.append(소개)
        b.append('csv')
        df_input.append(b)
        print(b)
    except:
        pass
    time.sleep(2)
    driver.close()

df = pd.DataFrame(df_input,columns = col)
df.to_csv('C:/Users/mdc_int_94/Desktop/data.csv',encoding='utf-8-sig',date_format= None)