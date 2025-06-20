import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=650305&no=417&week=sat')
soup = BeautifulSoup(driver.page_source,"html.parser")
