import time # 시간 지연
import random # 랜덤 선택 (게시글)
from selenium import webdriver #웹 브라우저 자동화 사용 
from selenium.webdriver.common.by import By #요소를 찾기 위한 기준 
from selenium.webdriver.common.keys import Keys #키 입력 사용 
from selenium.webdriver.support.ui import WebDriverWait #명시적 대기를 위한 클래스 
from selenium.webdriver.support import expected_conditions as EC # 특정 조건 충족 여부 체크

def instagram_automation(keyword):

    driver = webdriver.Chrome() # 크롬 브라우저 실행, 자동화 준비
    driver.implicitly_wait(10) # 요소를 찾을 때까지 최대 10초 기다림 (암묵적 대기)

    # 로그인
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)  # 로그인 페이지 로딩
    driver.find_element("name", "username").send_keys("consoleb.log")
    driver.find_element("name", "password").send_keys("dlthfqlalfqjsgh1209")
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(3)  # 로그인 처리 대기
    print("로그인 완료")

    # 3) 해시태그 페이지로 이동
    driver.get(f'https://www.instagram.com/explore/tags/{keyword}/')
    time.sleep(5)  # 포스트 로딩 대기

    # 4)  # 게시물의 링크를 모두 수집 (a 태그에서 '/p/'가 포함된 주소를 가진 것만)
    anchors = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    # 링크들을 href 속성으로부터 가져와 리스트로 만듦
    links = [a.get_attribute("href") for a in anchors]
    # 수집한 링크 중 하나를 랜덤으로 선택
    chosen = random.choice(links)
    # 선택된 게시물로 이동
    driver.get(chosen)

    wait = WebDriverWait(driver, 10) # 웹 요소가 로딩될 때까지 명확한 조건으로 기다려 주는 기능
    
    # 5) 좋아요 버튼 클릭
    try:
        like_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]/div/div/div') # 상대경로......못찾겠음.....
        like_btn.click()
        time.sleep(1)
        like_btn.click()  # 두 번 클릭해야됨
        print("좋아요 버튼 클릭 완료")
    except Exception as e:
        print("좋아요 버튼을 찾지 못했습니다.", e)

    # 6) 댓글 작성 
    try:
        textarea = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@aria-label, '댓글 달기')]"))
        ) # 웹 요소가 클릭 가능 상태인지 확인하는 조건 
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
