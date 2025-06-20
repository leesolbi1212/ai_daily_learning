# 구글 검색 자동화

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() #크롬브라우저를 컨트롤할 수 있게 함 
driver.get('https://www.google.com')
search = driver.find_element('name','q')
# find_element : element 속성을 찾아주는 메서드 name이 q인 것을 찾아라 
search.send_keys("날씨")
time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(10)

# 컴퓨터인게 걸려요 ㅠㅠ 해결방법?
