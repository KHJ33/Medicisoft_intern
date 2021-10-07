from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

#for 문 검색할 컬럼... 검은콩 등등

driver = webdriver.Chrome('/Users/kimhyunjo/Desktop/chromedriver')
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

elem = driver.find_element_by_name('q')

#검색에 들어갈 이름만 변경하시면 됩니다.
elem.send_keys('검은콩')

elem.send_keys(Keys.RETURN)

driver.find_element_by_css_selector('.rg_i.Q4LuWd').click()
time.sleep(2)
img_url = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')

#저장할 곳의 이름을 변경하시면 됩니다.
urllib.request.urlretrieve(img_url,'/Users/kimhyunjo/Desktop/test.jpg')

driver.close()

#이후에 데이터 프레임으로 저장
# list = [경로 참고]
# dataframe['경로'] = list