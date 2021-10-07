import requests
from bs4 import BeautifulSoup
import pandas as pd

array = []
# 500개의 데이터만 파싱하기 위해 50번 반복
for i in range(1, 51):
    # 각 페이지에 해당하는 url 요청
    url = 'https://www.saramin.co.kr/zf_user/company-review-qst-and-ans/sub?page='+str(i)+'&prev=sub&keyword=%EA%B1%B4%EA%B0%95&csn=&cat_mcls=&sort=reg_dt&influencerFl=n&searchType=&influencer='
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # 각 페이지의 상담 리스트 추출
        list = soup.select('#qst_and_ans_list > div > li')
        for li in list:
            content_array = []

            # 상담 내용과 날짜 추출
            content = li.select_one('span.qna_desc').text
            date = li.select_one('div.qna_data_infos > div > span').text.split('님이')[1].split(' 작성')[0].strip()
            # 각 상담의 내용과 날짜를 배열에 넣은 후 전체 배열에 삽입
            content_array.append(date)
            content_array.append(content)
            array.append(content_array)

df = pd.DataFrame(array, columns=['상담 날짜', '상담내용'])

df.to_csv('C:/Users/mdc_int_86/Desktop/0923사람인/사람인_커뮤니티_건강.csv',encoding='UTF-8-sig')