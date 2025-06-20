import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)   # 요소를 최대 10초까지 기다려 줌

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(3)

# 로그인 폼에 입력
username = driver.find_element("name", "username")
password = driver.find_element("name", "password")
username.send_keys("consoleb.log")
password.send_keys("dlthfqlalfqjsgh1209")

# 로그인 버튼 클릭
login_btn = driver.find_element("xpath", "//button[@type='submit']")
login_btn.click()

time.sleep(5)

print("로그인 완료")

