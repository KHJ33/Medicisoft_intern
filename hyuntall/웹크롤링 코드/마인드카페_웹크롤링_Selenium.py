from selenium import webdriver
import time

category_num = [8, 7, 6, 15, 2]
category_dict = {8: '자신감', 7: '대인관계', 6: '결혼', 15: '건강', 2: '진로취업'}
PATH = "C:/Users/mdc_int_86/Desktop/chromedriver"

for i in category_num:
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.mindcafe.co.kr/pc/community')

    driver.find_element_by_css_selector('#__next > div > div.community__FilterWraper-sc-49nndi-0.kQkTgK > div > div.Categories__CategoriesWrapper-sc-15qbxer-0.lbBSCZ > div.categories > div.categories__more > img').click()
    time.sleep(0.5)
    driver.find_element_by_css_selector(f'#__next > div > div.community__FilterWraper-sc-49nndi-0.kQkTgK > div > div.Categories__CategoriesWrapper-sc-15qbxer-0.czUTsg > div.categories > div.categories__groups > div:nth-child(2) > div.categories__group__menus > div:nth-child({i})').click()
    #카테고리 클릭

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)
    while 1:
        prev_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        curr_height = driver.execute_script("return document.body.scrollHeight")
        print("prev"+str(prev_height)+', curr'+str(curr_height))

        # 더이상 스크롤이 내려가지 않으면 break
        if curr_height == prev_height:
            break
        curr_height = prev_height

    file = open(f'C:/Users/mdc_int_86/Desktop/0923마인드카페/mindcafe_{category_dict[i]}.html', 'w',encoding='UTF-8')
    # 현재 크롬 브라우저에 나타나있는 html 요소 저장
    file.write(driver.page_source)
    file.close()
    driver.close()