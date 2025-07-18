# 스크롤 적용해서 리뷰 크롤링 해보기 

import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    
    scroll_count = 3
    for i in range(scroll_count):
        # 여기에 자바스크립트 문법을 쓰면 먹힘. (0부터 스크롤이 갈 수 있는 맨 아래 위치까지 내린다.)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div')
    # print(review_containers)
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')
    
    
    for i in range(len(review_containers)):
        review_text = review_containers[i].find('p', class_ = 'content-text').text
        # print(review_text)
        # print('-' * 30)
        date = review_date[i].text
        review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'})
        stars = 5 -len(review_empty_stars)
        # print(review_empty_stars)
        # print('-'*30)
        review_dict = {
            'review' : review_text,
            'stars' : stars,
            'date' : date
        }
        review_list.append(review_dict)
    return review_list
        
    
    
total_review = crawl_yanolja_reviews('힐스테이트 제주', 'https://nol.yanolja.com/reviews/domestic/10045919' )
print(total_review)

