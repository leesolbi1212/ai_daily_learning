import time                
# 프로그램 실행 중에 일시 정지할 때 쓰는 모듈
# 데이터를 표(테이블) 형태로 다룰 수 있게 해주는 pandas 모듈
from selenium import webdriver                                
# 웹 브라우저를 자동으로 제어하는 selenium의 webdriver
from selenium.webdriver import ActionChains                   
# 마우스 이동, 클릭 같은 복잡한 동작을 묶어 실행할 수 있게 해주는 클래스
from selenium.webdriver.common.by import By                   
# 요소를 찾을 때 사용하는 다양한 기준(By.ID, By.CSS_SELECTOR 등)을 불러옴
from selenium.webdriver.support.ui import WebDriverWait       
# 특정 조건이 만족될 때까지 대기하는 기능을 제공
from selenium.webdriver.support import expected_conditions as EC  
# 대기할 때 사용할 조건을 정의한 모듈
from bs4 import BeautifulSoup   
# HTML 문서를 파싱해서 원하는 정보를 쉽게 추출할 수 있게 해주는 BeautifulSoup를 불러옴
import re                       
# 정규 표현식(문자열 패턴 찾기/바꾸기)을 다룰 수 있게 해주는 모듈

def fetch_starbucks():
    # 1) 탐색할 스타벅스 홈페이지 주소를 변수에 저장
    starbucks_url = 'https://www.starbucks.co.kr/index.do'
    
    # 2) Chrome 브라우저를 켜는 드라이버 객체 생성
    driver = webdriver.Chrome()
    
    # 3) 브라우저 창을 최대화
    driver.maximize_window()
    
    # 4) 지정한 URL로 이동
    driver.get(starbucks_url)
    
    # 5) 페이지가 로딩될 시간을 1초 동안 기다림
    time.sleep(1)

    # 6) ActionChains 객체 생성 → 마우스 이동, 클릭 등을 연결해서 한 번에 실행할 수 있음
    action = ActionChains(driver)
    
    # 7) "매장 찾기" 메뉴에 마우스를 올리기 위해 해당 요소(첫 번째 태그)를 CSS 셀렉터로 찾아 저장
    first_tag = driver.find_element(
        By.CSS_SELECTOR,
        '#gnb > div > nav > div > ul > li.gnb_nav03 > h2 > a'
    )
    
    # 8) 서브 메뉴(매장 찾기 → 매장 찾기 클릭)의 두 번째 요소를 CSS 셀렉터로 찾아 저장
    second_tag = driver.find_element(
        By.CSS_SELECTOR,
        '#gnb > div > nav > div > ul > li.gnb_nav03 > div > div > div > '
        'ul:nth-child(1) > li:nth-child(3) > a'
    )
    
    # 9) 첫 번째 태그에 마우스를 올리고, 두 번째 태그에 마우스를 옮겨 클릭한 뒤 실행
    action.move_to_element(first_tag) \
          .move_to_element(second_tag) \
          .click() \
          .perform()
    
    # 10) 클릭 후 새로 뜨는 페이지가 로딩될 시간을 1초 기다림
    time.sleep(1)
    
    # 11) "서울" 지역 버튼이 클릭 가능해질 때까지 최대 10초 기다렸다가, 버튼 요소를 가져옴
    seoul_tag = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '#container > div > form > fieldset > div > section > '
            'article.find_store_cont > article > article:nth-child(4) > '
            'div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
        ))
    )
    
    # 12) 가져온 "서울" 버튼을 클릭
    seoul_tag.click()
    
    # --- 매장 정보를 담을 빈 리스트 생성 ---
    store_list = []  # 매장 이름
    addr_list  = []  # 매장 주소
    lat_list   = []  # 위도(latitude)
    lng_list   = []  # 경도(longitude)
    
    # 13) 구(區) 선택 버튼들이 로딩될 때까지 최대 5초 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'set_gugun_cd_btn'))
    )
    # 14) 모든 구 버튼 요소를 리스트로 가져옴
    gu_elements = driver.find_elements(By.CLASS_NAME, 'set_gugun_cd_btn')
    
    # 15) 전체 버튼이 클릭 가능해질 때까지 기다렸다가
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '#mCSB_2_container > ul > li:nth-child(1) > a'
        ))
    )
    # 16) 전체 버튼 클릭
    gu_elements[0].click()

    # 17) 매장 리스트(검색 결과)가 페이지에 나타날 때까지 최대 5초 기다림
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'quickResultLstCon'))
    )

    # 18) 현재 페이지의 HTML 전체를 문자열로 가져오기
    req = driver.page_source
    
    # 19) BeautifulSoup으로 HTML 파싱(분석) 준비
    soup = BeautifulSoup(req, 'html.parser')
    
    # 20) 매장 정보가 담긴 <ul> 태그 안의 <li> 태그들(각 매장)을 모두 찾아 리스트로 저장
    stores = soup.find(
        'ul', 'quickSearchResultBoxSidoGugun'
    ).find_all('li')

    # 21) 매장마다 정보를 꺼내서 리스트에 담기
    for store in stores:
        # 21.1) 매장 이름
        store_name = store.find('strong').text
        
        # 21.2) 매장 주소 (문자열)
        store_addr = store.find('p').text
        # 21.3) 끝에 붙은 전화번호(0000-0000) 제거하고 앞뒤 공백 정리
        store_addr = re.sub(r'\d{4}-\d{4}$', '', store_addr).strip()
        
        # 21.4) 위도, 경도 정보는 <li> 태그의 속성으로 저장되어 있음
        store_lat = store['data-lat']
        store_lng = store['data-long']
        
        # 21.5) 각각의 리스트에 추가
        store_list.append(store_name)
        addr_list.append(store_addr)
        lat_list.append(store_lat)
        lng_list.append(store_lng)

    # 22) 수집한 리스트들을 한 번에 DataFrame(표)로 변환
    df = pd.DataFrame({
        'store': store_list,
        'addr' : addr_list,
        'lat'  : lat_list,
        'lng'  : lng_list
    })

    # 23) 브라우저 닫기
    driver.quit()
    
    # 24) 완성된 DataFrame 리턴(함수 밖으로 전달)
    return df

starbucks_df = fetch_starbucks()
starbucks_df.to_csv('starbucks_seoul.csv', index=False, encoding='utf-8-sig')
print("데이터가 starbucks_seoul.csv 파일로 저장되었습니다.")
