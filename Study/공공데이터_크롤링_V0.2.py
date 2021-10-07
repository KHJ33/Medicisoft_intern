import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['카테고리','제목', '내용'])

for page_move in range(1,27):
    URL = 'http://www.bizk.co.kr/board_new/?page='+str(page_move)+'&cate1=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&flag=n&view_all=&cate2=%EC%B0%BD%EC%97%85%EC%9D%B4%EC%95%BC%EA%B8%B0&cate3=%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90%2F%EC%B0%BD%EC%97%85%EC%9D%B4%EC%95%BC%EA%B8%B0%2F%EC%B0%BD%EC%97%85%EC%95%84%EC%9D%B4%ED%85%9C%ED%99%8D%EB%B3%B4'
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')

    title = soup.find_all(class_='title_line')

    basic_url = 'http://www.bizk.co.kr/board_new'
    for i in title:
        #print(i.get_text())
        if i.find(class_='gray') == None:
            a = i.find('a')
            a = basic_url + a.attrs['href'][1:]
            print(a)
            html = requests.get(a)
            soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')

            text = soup.find(class_='view_text')
            #print(text.get_text().strip()[:-1])
            df = df.append(
                {'카테고리': 'group_name.get_text()', '제목': i.get_text(), '내용':text.get_text().strip()[:-1]},
                ignore_index=True)
df.to_csv('C:/Users/mdc_int_94/Desktop/창업.csv',encoding='utf-8-sig')
