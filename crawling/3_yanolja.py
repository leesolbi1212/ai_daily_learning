# 스크롤 적용해서 리뷰 크롤링 해보기 

import time
from selenium import webdriver

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    
    scroll_count = 