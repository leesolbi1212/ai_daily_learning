import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def instagram_automation(keyword):

    driver = webdriver.Chrome()
    driver.implicitly_wait(10) 

    # 로그인
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)  # 로그인 페이지 로딩
    driver.find_element("name", "username").send_keys("consoleb.log")
    driver.find_element("name", "password").send_keys("dlthfqlalfqjsgh1209")
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(5)  # 로그인 처리 대기
    print("로그인 완료")

    # 3) 해시태그 페이지로 이동
    driver.get(f'https://www.instagram.com/explore/tags/{keyword}/')
    time.sleep(5)  # 포스트 로딩 대기

    # 4) 게시물 링크 수집 랜덤 선택
    anchors = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    links = [a.get_attribute("href") for a in anchors]
    chosen = random.choice(links)
    driver.get(chosen)

    wait = WebDriverWait(driver, 10)
    # 5) 좋아요 버튼 클릭
    try:
        like_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]/div/div/div')
        like_btn.click()
        time.sleep(1)
        like_btn.click()  # 두 번 클릭하려면 한 번 더 (실제 기능 확인 필요)
        print("좋아요 버튼 클릭 완료")
    except Exception as e:
        print("좋아요 버튼을 찾지 못했습니다.", e)

    # 6) 댓글 작성 
    try:
        textarea = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@aria-label, '댓글 달기')]"))
        )
        textarea.click()
        time.sleep(1)
        textarea = driver.find_element(By.XPATH, "//textarea[contains(@aria-label, '댓글 달기')]")
        textarea.send_keys("우와 너무 맛있겠어요!")
        textarea.send_keys(Keys.ENTER)
        print("댓글 완료")
    except Exception as e:
        print("댓글 입력창을 찾지 못했습니다.", e)

    # 7) 브라우저 종료 전 대기
    input("브라우저를 종료합니다")
    driver.quit()

if __name__ == "__main__":
    instagram_automation("양재시민의숲맛집")
