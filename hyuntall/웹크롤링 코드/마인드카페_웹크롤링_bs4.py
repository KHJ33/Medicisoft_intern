from bs4 import BeautifulSoup
import pandas as pd
import requests

categorys = ['자신감', '대인관계', '결혼', '건강', '진로취업']


for category in categorys:
    data = open(f'C:/Users/mdc_int_86/Desktop/0923마인드카페/mindcafe_{category}.html','r',encoding='UTF-8')
    soup = BeautifulSoup(data, 'html.parser')
    stories = soup.select('#__next > div > div.community__HomeWrapper-sc-49nndi-1.iskGzP > div > div.Stories__StoriesWrapper-clu9ot-0.enwmNA > div.stories > div > div > div.main > a.contents')

    urls = []
    array = []
    # 각각의 상담 제목에서 상담 내용에 해당하는 url 추출
    for title in stories:
        url = title['href']
        urls.append(url)

    content_array = []
    # 각 url마다 request를 통해 웹사이트 데이터 요청
    for url in urls:
        response = requests.get('https://www.mindcafe.co.kr'+url)
        if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # 날짜 정보에 해당하는 컴포넌트 요소 배열 추출
                dates = soup.select('#__next > div > div.story__StoryWrapper-sc-6x53gv-1.jNgght.page > div.story.card > div.header > div.info > div.from-now')
                # 제목에 해당하는 컴포넌트 요소 배열 추출
                titles = soup.select('#__next > div > div.story__StoryWrapper-sc-6x53gv-1.jNgght.page > div.story.card > div.main > div.main__title')
                # 상담 내용에 해당하는 컴포넌트 요소 배열 추출
                contents = soup.select('#__next > div > div.story__StoryWrapper-sc-6x53gv-1.jNgght.page > div.story.card > div.main > div.main__contents')
                content_array = []
                date = dates[0].text
                try:
                    # 제목과 내용요소가 둘 다 있을 경우 내용에 포함시킨다.
                    content = titles[0].text+ " " +contents[0].text
                except:
                    # 제목 요소가 없으면 내용만 포함시킨다.
                    content = contents[0].text

                content_array.append(date)
                content_array.append(content)
                content_array.append('https://www.mindcafe.co.kr'+url)
                # 상담에 필요한 요소들을 배열에 넣은 후 전체 배열에 삽입
                array.append(content_array)

    df = pd.DataFrame(array, columns=['상담 날짜', '상담내용', 'url'])
    df.to_csv(f'C:/Users/mdc_int_86/Desktop/a/mindcafe_{category}.csv',encoding='UTF-8-sig')