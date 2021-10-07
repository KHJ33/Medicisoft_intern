import requests
from bs4 import BeautifulSoup
import pandas as pd

col = ['목록', '검색명', '데이터 형태', '데이터 형식', '설명', '키워드']
df_file = pd.DataFrame()
category = '문화'

dict = {}
data_list = []
File_page =170
for i in range(1, File_page):
    URL = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EB%AC%B8%ED%99%94&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='+str(i)+'&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')

    result_list = soup.find(class_='result-list').find_all('li')

    print(i)
    for k in result_list:
        page_data_list = []
        tagset_json = k.find(class_='tagset json')
        if tagset_json:
            tagset_json = 'CSV, ' + tagset_json.get_text().strip()
        else:
            tagset_json = 'CSV'

        title = k.find(class_='title').get_text().strip()
        content = k.find(class_='ellipsis publicDataDesc').get_text().strip()

        key_word = k.find(class_='info-data').find_all('p')[-1]
        key_word = key_word.get_text().split()[-1]

        if (category in title) or (category in key_word):
            if title not in dict:
                dict[title] = 0
                page_data_list.append(title)
                page_data_list.append(category)
                page_data_list.append('파일데이터')
                page_data_list.append(tagset_json)
                page_data_list.append(content)
                page_data_list.append(key_word)

                data_list.append(page_data_list)

df_file = pd.DataFrame(data_list, columns=col)

print('API 부분======')
df_API = pd.DataFrame()
dict = {}
data_list = []
API_page = 26
for i in range(1, API_page):

    URL = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EB%AC%B8%ED%99%94&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='+str(i)+'&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')

    result_list = soup.find(class_='result-list').find_all('li')
    print(i)
    for k in result_list:
        page_data_list = []
        tagset_json = k.find(class_='tagset json')
        if tagset_json:
            tagset_json = 'XML, ' + tagset_json.get_text().strip()
        else:
            tagset_json = 'XML'

        title = k.find(class_='title').get_text().strip()
        content = k.find(class_='ellipsis publicDataDesc').get_text().strip()

        key_word = k.find(class_='info-data').find_all('p')[-1]
        key_word = key_word.get_text().split()[-1]

        if (category in title) or (category in key_word):
            if title not in dict:
                dict[title] = 0
                page_data_list.append(title)
                page_data_list.append(category)
                page_data_list.append('오픈API')
                page_data_list.append(tagset_json)
                page_data_list.append(content)
                page_data_list.append(key_word)

                data_list.append(page_data_list)

df_API = pd.DataFrame(data_list, columns=col)

df_result = pd.concat([df_file,df_API])
df_result = df_result.sort_values(by=['목록'],axis=0)
df_result = df_result.reset_index(drop=True)
df_result.to_csv('C:/Users/mdc_int_94/Desktop/'+category+'.csv',encoding='utf-8-sig')