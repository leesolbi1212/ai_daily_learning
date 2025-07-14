# 좋아요는 안누름 
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def instagram_automation(keyword, num_comments=10):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # 1) 로그인
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    driver.find_element("name", "username").send_keys("consoleb.log")
    driver.find_element("name", "password").send_keys("dlthfqlalfqjsgh1209")
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(5)
    print("로그인 완료")

    # 2) 해시태그 페이지로 이동 & 게시물 링크 수집
    driver.get(f'https://www.instagram.com/explore/tags/{keyword}/')
    time.sleep(5)
    anchors = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    links = [a.get_attribute("href") for a in anchors]

    wait = WebDriverWait(driver, 10)

    # 3) 댓글 반복 수행
    for i in range(num_comments):
        link = random.choice(links)
        driver.get(link)
        time.sleep(3)

        try:
            textarea = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@aria-label, '댓글 달기')]"))
            )
            textarea.click()
            time.sleep(1)
            textarea = driver.find_element(By.XPATH, "//textarea[contains(@aria-label, '댓글 달기')]")
            textarea.send_keys("단발머리가 너무 잘 어울리시네요!")
            textarea.send_keys(Keys.ENTER)
            print(f"{i+1}번째 댓글 완료 ▶ {link}")
        except Exception as e:
            print(f"{i+1}번째 댓글 실패 ▶ {e}")

        time.sleep(2)

    input("모든 댓글 완료. 종료하려면 Enter를 누르세요.")
    driver.quit()

if __name__ == "__main__":
    instagram_automation("단발머리")  
