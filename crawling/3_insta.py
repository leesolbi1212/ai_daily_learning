import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# EC : 특정 조건을 기다릴 때 사용
from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait : 조건이 충족될 때까지 기기
from selenium.webdriver.support.ui import WebDriverWait
Instargram = 'https://www.instagram.com/'
def like_pass(tag, num):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Instargram)
    time.sleep(5)
    id_box = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'
    )))
    my_id = 'gw_ju_le'
    id_box.send_keys(my_id)
    time.sleep(5)
    password_box = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'
    )))
    my_password = 'qwer1234!@#$'
    password_box.send_keys(my_password)
    time.sleep(5)
    login_btn = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'
    )))
    login_btn.click()
    time.sleep(5)
    tag_what = 'https://www.instagram.com/explore/search/keyword/?q=%23' + tag
    driver.get(tag_what)
    time.sleep(5)
    post_btn = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@role="main"]//following :: div[4] //following :: div[1]'
    )))
    post_btn.click()
    time.sleep(5)
    for i in range(num):
        like_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: div[3]'
        )))
        like_btn.click()
        time.sleep(5)
        like_btn.click()
        time.sleep(5)
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']"))
        )
        time.sleep(5)
        comment_box.click()
        time.sleep(5)
        active_comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='댓글 달기...' and @data-focus-visible-added]"))
        )
        active_comment_box.send_keys("학원 끝나면 꼭 한번 먹으러 가고싶어요.")
        post_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Post')]"))
        )
        post_button.click()
        time.sleep(3)
        next_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="다음" and @height="16" and @width="16"]'
        )))
        next_btn.click()
        time.sleep(5)
    print(f'{tag} 로 검색 후 {num}번 좋아요를 눌렀어요!')
like_pass('역삼맛집', 3)