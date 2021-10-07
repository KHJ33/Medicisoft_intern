import requests
import pandas as pd
from bs4 import BeautifulSoup


count = 0
df = pd.DataFrame(columns=['제목', '내용'])
for i in range(1, 100):
    URL = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%ED%86%B5%EB%9F%89&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='+str(i)+'&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')

    li = soup.find(class_='result-list').find_all('li')
    for k in li:
        title = k.find(class_='title')
        title_text = title.get_text().strip()
        content = k.find(class_='ellipsis publicDataDesc')
        content_text = content.get_text().strip()
        if '수도권' not in title_text:
            if '교통량' in content_text:
                print(title_text)
                df = df.append({'제목': title_text, '내용': content_text},ignore_index=True)
df.to_csv('C:/Users/mdc_int_94/Desktop/공공데이터1.csv',encoding='utf-8-sig')