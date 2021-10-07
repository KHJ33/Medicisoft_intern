import requests
from bs4 import BeautifulSoup
import pandas as pd

col = ['제목', '저자', '자료이용장소']
data_list = []
for i in range(1, 61):
    print(i)

    URL = 'https://www.nl.go.kr/NL/contents/search.do?resultType=&pageNum=' + str(
        i) + '&pageSize=10&order=&sort=&srchTarget=total&kwd=%EA%B3%A0%EB%AC%B8%ED%97%8C&systemType=&lnbTypeName=&category=%EB%8F%84%EC%84%9C&hanjaFlag=&reSrchFlag=&licYn=&kdcName1s=&manageName=&langName=&ipubYear=&pubyearName=&seShelfCode=&detailSearch=&seriesName=&mediaCode=&offerDbcode2s=&f1=&v1=&f2=&v2=&f3=&v3=&f4=&v4=&and1=&and2=&and3=&and4=&and5=&and6=&and7=&and8=&and9=&and10=&and11=&and12=&isbnOp=&isbnCode=&guCode2=&guCode3=&guCode4=&guCode5=&guCode6=&guCode7=&guCode8=&guCode11=&gu2=&gu7=&gu8=&gu9=&gu10=&gu12=&gu13=&gu14=&gu15=&gu16=&subject=&sYear=&eYear=&sRegDate=&eRegDate=&typeCode=&acConNo=&acConNoSubject=&infoTxt='
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')

    row = soup.find_all(class_='row')
    for k in row:
        a = []
        title = k.find(class_='txt_left row_txt_tit').get_text().split('\n')[1]
        # print(title.get_text())

        txt_grey = k.find_all(class_='mr txt_grey')
        text = ''
        for t in txt_grey:
            if text == '':
                text = t.get_text()
            else:
                text += '\n' + t.get_text()
        txt_black = k.find_all(class_='comments txt_black')[0].get_text()
        comments = k.find(class_='txt_link txt_orange btn_layer').get_text()
        # print(text)
        a.append(title)
        a.append(text)
        a.append(comments)
        # print(len(a))
        data_list.append(a)


df = pd.DataFrame(data_list, columns=col)
df.to_csv('C:/Users/mdc_int_94/Desktop/국립중앙도서관.csv', encoding='utf-8-sig', date_format=None)