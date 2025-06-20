import time
from selenium import webdriver
from selenium.webdriver.common.by import By #파싱하는 종류들을 상수화
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=650305&no=417&week=sat')
soup = BeautifulSoup(driver.page_source,"html.parser")
time.sleep(2)

print('**베스트 댓글**')
xpath = '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul/li'
best_comment_elements = driver.find_elements(By.XPATH, xpath)

for li in best_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, './div/div[2]/div/p') # xpath 이후의 경로를 작성해줘야 함 
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except Exception as e:
        print(e)