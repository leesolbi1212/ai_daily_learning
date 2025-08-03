import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
import pandas as pd
from openpyxl import Workbook

# ----------------------------------------
# 설정 및 유틸
# ----------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

# ----------------------------------------
# YES24 크롤러
# ----------------------------------------
def crawl_yes24(keyword, pages, driver):
    """
    YES24 검색 결과를 크롤링하여
    초기 검색은 검색창 입력을 통해, 2페이지 이후는 페이지 버튼 클릭으로 이동
    이미지 파일을 로컬에 저장하고 메타데이터 리스트를 반환
    """
    encoded_kw = quote_plus(keyword)
    image_folder = os.path.join(BASE_DIR, 'images', 'yes24')
    ensure_folder(image_folder)
    results = []
    image_failures = 0

    # 1) 홈페이지 접속 및 초기 검색
    driver.get("https://www.yes24.com/")
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, 'button.layerClose').click()
        time.sleep(0.5)
    except NoSuchElementException:
        pass
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#query')
    search_box.click(); search_box.clear(); search_box.send_keys(keyword); search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    # 2) 페이지별 크롤링 (1페이지는 이미 로딩됨)
    for page in range(1, pages + 1):
        if page > 1:
            try:
                print(f"[YES24] 페이지 {page}로 이동 시도...")
                
                # 페이지네이션 영역 찾기 (여러 가능한 셀렉터 시도)
                pagination_selectors = [
                    'div.yesUI_pagen',
                    'div.yesUl_pagen',
                    'div.pagination',
                    'div.page_navi',
                    'div.yesUI_pagen ul',
                    'div.yesUl_pagen ul'
                ]
                
                pagination = None
                for selector in pagination_selectors:
                    try:
                        pagination = WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                        )
                        print(f"[YES24] 페이지네이션 찾음: {selector}")
                        break
                    except:
                        continue
                
                if not pagination:
                    print(f"[YES24] 페이지네이션을 찾을 수 없음")
                    break
                
                # 페이지네이션 영역으로 스크롤
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", pagination)
                time.sleep(1)
                
                # 페이지 번호 링크 찾기 (여러 방법 시도)
                page_btn = None
                page_selectors = [
                    f"a.num[title='{page}']",
                    f"a[title='{page}']",
                    f"a:contains('{page}')",
                    f"a[href*='page={page}']",
                    f"a[onclick*='{page}']"
                ]
                
                for selector in page_selectors:
                    try:
                        page_btn = WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        print(f"[YES24] 페이지 {page} 버튼 찾음: {selector}")
                        break
                    except:
                        continue
                
                # 텍스트로 직접 찾기
                if not page_btn:
                    all_links = pagination.find_elements(By.CSS_SELECTOR, 'a')
                    for link in all_links:
                        if link.text.strip() == str(page):
                            page_btn = link
                            print(f"[YES24] 페이지 {page} 버튼 찾음 (텍스트)")
                            break
                
                if page_btn:
                    # 클릭 가능할 때까지 대기
                    WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(page_btn)
                    )
                    page_btn.click()
                    print(f"[YES24] 페이지 {page} 클릭 완료")
                    
                    # 페이지 로딩 대기
                    time.sleep(2)
                    
                    # 결과 리스트가 로드될 때까지 대기
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul#yesSchList'))
                    )
                    time.sleep(1)
                else:
                    print(f"[YES24] 페이지 {page} 버튼을 찾을 수 없음")
                    break
            except Exception as e:
                print(f"[YES24] 페이지 {page} 이동 실패: {e}")
                break

        # 3) 리스트 아이템 수집
        items = driver.find_elements(By.CSS_SELECTOR, 'ul#yesSchList > li')
        print(f"[YES24] Page {page}: found {len(items)} items")

        for item in items:
            entry = {'검색어': keyword, '책제목': '', '저자': '', '가격': '', '출판사': '', '출판일': '', '이미지_경로': '', '이미지_상태': '성공'}
            
            # 책제목
            try: 
                entry['책제목'] = item.find_element(By.CSS_SELECTOR, 'div.info_row.info_name a').text.strip()
            except: pass
            
            # 저자 - span.authPub.info_auth에서 추출
            try:
                author_elem = item.find_element(By.CSS_SELECTOR, 'span.authPub.info_auth')
                entry['저자'] = author_elem.text.strip()
            except:
                entry['저자'] = ''

            # 출판사 - span.authPub.info_pub > a에서 추출
            try:
                pub_elem = item.find_element(By.CSS_SELECTOR, 'span.authPub.info_pub a')
                entry['출판사'] = pub_elem.text.strip()
            except:
                entry['출판사'] = ''

            # 출판일 - span.authPub.info_date에서 추출
            try:
                date_elem = item.find_element(By.CSS_SELECTOR, 'span.authPub.info_date')
                entry['출판일'] = date_elem.text.strip()
            except:
                entry['출판일'] = ''

            # 가격 - 정확한 셀렉터로 추출 (0원 방지)
            try:
                # 가장 정확한 가격 셀렉터로 시도
                price_elem = item.find_element(By.CSS_SELECTOR, 'div.info_row.info_price strong.txt_num em.yes_b')
                price_text = price_elem.text.strip()
                import re
                price_match = re.search(r'[\d,]+', price_text)
                if price_match:
                    price_number = price_match.group()
                    entry['가격'] = f"{price_number}원"
                else:
                    entry['가격'] = price_text
            except:
                # 백업: 기존 방식
                try:
                    price_elem = item.find_element(By.CSS_SELECTOR, 'em.yes_b')
                    price_text = price_elem.text.strip()
                    import re
                    price_match = re.search(r'[\d,]+', price_text)
                    if price_match:
                        price_number = price_match.group()
                        entry['가격'] = f"{price_number}원"
                    else:
                        entry['가격'] = price_text
                except:
                    entry['가격'] = ''
            
            # 이미지 다운로드 - 셀렉터 수정
            try:
                # YES24의 실제 이미지 구조 확인
                img_selectors = [
                    'div.img_box img',
                    'span.img_box img',
                    'div.item_img img',
                    'img[data-original]',
                    'img[data-src]',
                    'img[src*="image.yes24.com"]',
                    'img[src*="yes24.com"]',
                    'img'
                ]
                img_elem = None
                for selector in img_selectors:
                    try:
                        img_elem = item.find_element(By.CSS_SELECTOR, selector)
                        if img_elem:
                            src = img_elem.get_attribute('src') or img_elem.get_attribute('data-original') or img_elem.get_attribute('data-src')
                            if src and ('image.yes24.com' in src or 'yes24.com' in src):
                                break
                    except NoSuchElementException:
                        continue
                
                if img_elem:
                    driver.execute_script("arguments[0].scrollIntoView(true);", img_elem)
                    time.sleep(0.1)
                    src = img_elem.get_attribute('data-original') or img_elem.get_attribute('data-src') or img_elem.get_attribute('src')
                    if src.startswith('//'): src = 'https:' + src
                    
                    # 유효한 이미지 URL인지 확인
                    if src and ('image.yes24.com' in src or 'yes24.com' in src):
                        ext = os.path.splitext(src.split('?')[0])[1] or '.jpg'
                        safe = ''.join(c for c in entry['책제목'] if c.isalnum() or c in ' _-')[:50]
                        local = os.path.join(image_folder, safe + ext)
                        resp = requests.get(src, timeout=10)
                        resp.raise_for_status()
                        with open(local, 'wb') as f: f.write(resp.content)
                        entry['이미지_경로'] = local
                    else:
                        raise Exception('유효하지 않은 이미지 URL')
                else:
                    raise Exception('이미지 요소를 찾을 수 없음')
            except Exception as e:
                image_failures += 1
                entry['이미지_상태'] = f'실패: {e}'

            results.append(entry)
            print(f"[YES24] Parsed: {entry['책제목']} (Image: {entry['이미지_상태']})")

    print(f"[YES24] Total items: {len(results)}, Image failures: {image_failures}")
    return results

# ----------------------------------------
# 교보문고 크롤러
# ----------------------------------------
def crawl_kyobo(keyword, pages, driver):
    """
    교보문고 검색 결과를 크롤링하여
    이미지 파일을 로컬에 저장하고 메타데이터 리스트를 반환
    """
    encoded_kw = quote_plus(keyword)
    base_search = "https://search.kyobobook.co.kr/search?keyword={kw}&gbCode=TOT&target=total&page={pg}"
    image_folder = os.path.join(BASE_DIR, 'images', 'kyobo')
    ensure_folder(image_folder)
    results = []
    image_failures = 0

    for page in range(1, pages + 1):
        url = base_search.format(kw=encoded_kw, pg=page)
        print(f"[KYOB] Navigating to: {url}")
        driver.get(url)
        time.sleep(2)

        # 상품 리스트 요소
        items = driver.find_elements(By.CSS_SELECTOR, 'div#shopData_list ul.prod_list > li.prod_item')
        print(f"[KYOB] Page {page}: found {len(items)} items")

        for item in items:
            entry = {'검색어': keyword, '책제목': '', '저자': '', '가격': '', '출판사': '', '출판일': '', '이미지_경로': '', '이미지_상태': '성공'}
            # 제목
            try:
                entry['책제목'] = item.find_element(By.CSS_SELECTOR, 'div.auto_overflow_wrap.prod_name_group').text.strip()
            except:
                pass
            # 저자 - 이미지 참고: <a class="author rep"> 또는 <a class="author">
            try:
                author_elements = item.find_elements(By.CSS_SELECTOR, 'div.auto_overflow_inner a.author')
                if author_elements:
                    authors = [elem.text.strip() for elem in author_elements if elem.text.strip()]
                    entry['저자'] = ', '.join(authors)
            except:
                pass
            # 출판사 및 출판일 - 이미지 참고: <a class="text">와 <span class="date">
            try:
                # 출판사: <a class="text"> 태그에서 추출
                publisher_elem = item.find_element(By.CSS_SELECTOR, 'div.prod_publish a.text')
                if publisher_elem:
                    entry['출판사'] = publisher_elem.text.strip()
            except:
                pass
            try:
                # 출판일: <span class="date"> 태그에서 추출
                date_elem = item.find_element(By.CSS_SELECTOR, 'div.prod_publish span.date')
                if date_elem:
                    entry['출판일'] = date_elem.text.strip()
            except:
                pass
            # 가격 - 이미지 참고: <span class="val"> + <span class="unit"> 구조
            try:
                # 숫자 부분: <span class="val">
                price_val_elem = item.find_element(By.CSS_SELECTOR, 'div.prod_price span.price span.val')
                price_number = price_val_elem.text.strip()
                
                # 통화 단위 부분: <span class="unit"> (보통 "원" 포함)
                price_unit_elem = item.find_element(By.CSS_SELECTOR, 'div.prod_price span.price span.unit')
                price_unit = price_unit_elem.text.strip()
                
                # 숫자와 단위 조합
                if price_number and price_unit:
                    entry['가격'] = f"{price_number}{price_unit}"
                elif price_number:
                    entry['가격'] = f"{price_number}원"
                else:
                    entry['가격'] = ''
            except:
                # 백업: 기존 방식
                try:
                    entry['가격'] = item.find_element(By.CSS_SELECTOR, 'div.prod_price > strong').text.strip()
                except:
                    entry['가격'] = ''
            # 이미지 로드 & 다운로드
            try:
                from selenium.webdriver.common.action_chains import ActionChains
                img_elem = item.find_element(By.CSS_SELECTOR, 'span.img_box img')
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", img_elem)
                time.sleep(0.5)
                if img_elem.get_attribute('loading') == 'lazy':
                    ActionChains(driver).move_to_element(img_elem).perform()
                    time.sleep(0.5)
                src = img_elem.get_attribute('data-src') or img_elem.get_attribute('src')
                if src.startswith('//'):
                    src = 'https:' + src
                if 'img_ready' in src or 'prepare' in src:
                    raise Exception('placeholder image')
                ext = os.path.splitext(src.split('?')[0])[1] or '.jpg'
                safe = ''.join(c for c in entry['책제목'] if c.isalnum() or c in ' _-')[:50]
                local = os.path.join(image_folder, safe + ext)
                if not os.path.exists(local):
                    resp = requests.get(src, timeout=10)
                    resp.raise_for_status()
                    with open(local, 'wb') as f:
                        f.write(resp.content)
                entry['이미지_경로'] = local
            except Exception as e:
                image_failures += 1
                entry['이미지_상태'] = f'실패: {e}'

            results.append(entry)
            print(f"[KYOB] Parsed: {entry['책제목']} (Image: {entry['이미지_상태']})")

    print(f"[KYOB] Total items: {len(results)}, Image failures: {image_failures}")
    return results

# ----------------------------------------
# 알라딘 크롤러 (수정된 버전)
# ----------------------------------------
def crawl_aladin(keyword, pages, driver):
    """
    알라딘 검색 결과를 크롤링하여
    이미지 파일을 로컬에 저장하고 메타데이터 리스트를 반환
    """
    encoded_kw = quote_plus(keyword)
    base_url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={encoded_kw}"
    image_folder = os.path.join(BASE_DIR, 'images', 'aladin')
    ensure_folder(image_folder)
    results = []
    image_failures = 0

    # 초기 페이지 로드
    driver.get(base_url)
    time.sleep(2)

    for page in range(1, pages + 1):
        if page > 1:
            try:
                # 페이지네이션 개선
                pagination = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div#short > div.numbox'))
                )
                # 페이지네이션 영역을 화면 상단에 오도록 스크롤
                driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", pagination)
                time.sleep(1)
                
                # 페이지 번호로 직접 링크 찾기 (개선된 방식)
                page_links = pagination.find_elements(By.CSS_SELECTOR, 'a')
                target_link = None
                
                # 1. 텍스트로 직접 찾기
                for link in page_links:
                    if link.text.strip() == str(page):
                        target_link = link
                        print(f"[ALADIN] 페이지 {page} 링크 찾음 (텍스트)")
                        break
                
                # 2. href 속성에서 페이지 번호 찾기
                if not target_link:
                    for link in page_links:
                        href = link.get_attribute('href') or ''
                        if f'page={page}' in href or f'Page={page}' in href:
                            target_link = link
                            print(f"[ALADIN] 페이지 {page} 링크 찾음 (href)")
                            break
                
                # 3. onclick 속성에서 페이지 번호 찾기
                if not target_link:
                    for link in page_links:
                        onclick = link.get_attribute('onclick') or ''
                        if str(page) in onclick:
                            target_link = link
                            print(f"[ALADIN] 페이지 {page} 링크 찾음 (onclick)")
                            break
                
                # 4. 다음 페이지 버튼 찾기 (순차 이동)
                if not target_link and page == 2:
                    for link in page_links:
                        if '다음' in link.text or 'next' in link.text.lower():
                            target_link = link
                            print(f"[ALADIN] 다음 페이지 버튼 찾음")
                            break
                
                if target_link:
                    # 클릭 가능할 때까지 대기
                    WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(target_link)
                    )
                    target_link.click()
                    print(f"[ALADIN] 페이지 {page} 클릭 완료")
                    time.sleep(2)
                    
                    # 페이지 로딩 대기
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#Search3_Result'))
                    )
                    time.sleep(1)
                else:
                    print(f"[ALADIN] Page {page} 링크를 찾을 수 없음, 현재 페이지에서 계속")
                    break
            except Exception as e:
                print(f"[ALADIN] 페이지 {page} 이동 실패: {e}")
                break

        print(f"[ALADIN] Page {page} loaded")
        # 도서 박스 리스트 선택
        boxes = driver.find_elements(By.CSS_SELECTOR, 'div#Search3_Result > div.ss_book_box')
        print(f"[ALADIN] Page {page}: found {len(boxes)} items")
        
        for box in boxes:
            entry = {'검색어': keyword, '책제목': '', '저자': '', '가격': '', '출판사': '', '출판일': '', '이미지_경로': '', '이미지_상태': '성공'}
            # 제목
            try:
                entry['책제목'] = box.find_element(By.CSS_SELECTOR, 'div.ss_book_list ul li span.tit_category + a.bo3').text.strip()
            except:
                pass
            # 저자, 출판사, 출판일 - li[2] 내부에서 추출
            try:
                info_li = box.find_element(By.CSS_SELECTOR, 'div.ss_book_list ul li:nth-child(2)')
                a_tags = info_li.find_elements(By.TAG_NAME, 'a')
                # 저자
                entry['저자'] = a_tags[0].text.strip() if len(a_tags) > 0 else ''
                # 출판사
                entry['출판사'] = a_tags[1].text.strip() if len(a_tags) > 1 else ''
                # 출판일: li 전체 텍스트에서 마지막 '|' 뒤의 값
                info_text = info_li.text.strip()
                if '|' in info_text:
                    entry['출판일'] = info_text.split('|')[-1].strip()
                else:
                    entry['출판일'] = ''
            except:
                entry['저자'] = ''
                entry['출판사'] = ''
                entry['출판일'] = ''
            # 가격 - li[3] > span[1]에서 추출 (0원 방지)
            try:
                price_elem = box.find_element(By.CSS_SELECTOR, 'div.ss_book_list ul li:nth-child(3) > span:nth-child(1)')
                price_text = price_elem.text.strip()
                import re
                price_match = re.search(r'[\d,]+', price_text)
                if price_match:
                    price_number = price_match.group()
                    entry['가격'] = f"{price_number}원"
                else:
                    entry['가격'] = price_text
            except:
                # 백업: 기존 방식
                try:
                    price_li = box.find_element(By.CSS_SELECTOR, 'div.ss_book_list ul li span.ss_p2')
                    entry['가격'] = price_li.text.strip()
                except:
                    entry['가격'] = ''
            # 이미지 다운로드 - 셀렉터 개선
            try:
                # 여러 가능한 이미지 셀렉터 시도
                img_selectors = [
                    'div.cover_area img.front_cover',
                    'div.cover_area img',
                    'img.front_cover',
                    'img[src*="aladin.co.kr"]'
                ]
                img_elem = None
                for selector in img_selectors:
                    try:
                        img_elem = box.find_element(By.CSS_SELECTOR, selector)
                        break
                    except NoSuchElementException:
                        continue
                
                if img_elem:
                    driver.execute_script("arguments[0].scrollIntoView(true);", img_elem)
                    src = img_elem.get_attribute('src')
                    if src.startswith('//'): src = 'https:' + src
                    ext = os.path.splitext(src.split('?')[0])[1] or '.jpg'
                    safe = ''.join(c for c in entry['책제목'] if c.isalnum() or c in ' _-')[:50]
                    filename = safe + ext
                    local = os.path.join(image_folder, filename)
                    if not os.path.exists(local):
                        resp = requests.get(src, timeout=10)
                        resp.raise_for_status()
                        with open(local, 'wb') as f:
                            f.write(resp.content)
                    entry['이미지_경로'] = local
                else:
                    raise Exception('이미지 요소를 찾을 수 없음')
            except Exception as e:
                image_failures += 1
                

            results.append(entry)
            print(f"[ALADIN] Parsed: {entry['책제목']} (Image: {entry['이미지_상태']})")

    print(f"[ALADIN] Total items: {len(results)}, Image failures: {image_failures}")
    return results

# 통합 크롤링 함수
# ----------------------------------------
def crawl_all(keyword, yes24_pages, kyobo_pages, aladin_pages):
    """
    세 사이트(YES24, 교보문고, 알라딘)를 순차 크롤링하고
    결과 리스트 3개를 반환
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        yes24 = crawl_yes24(keyword, yes24_pages, driver)
        kyobo = crawl_kyobo(keyword, kyobo_pages, driver)
        aladin = crawl_aladin(keyword, aladin_pages, driver)
    finally:
        driver.quit()
    return yes24, kyobo, aladin

# 엑셀 저장 함수
# ----------------------------------------
def save_to_excel(yes24_list, kyobo_list, aladin_list, keyword):
    """
    크롤링 결과를 엑셀 파일로 저장 (이미지_상태 컬럼은 저장하지 않음)
    """
    filename = f"{keyword}_books_new.xlsx"

    # 이미지_상태 컬럼 제거
    def remove_image_status(data):
        return [
            {k: v for k, v in item.items() if k != '이미지_상태'}
            for item in data
        ]

    yes24_clean = remove_image_status(yes24_list)
    kyobo_clean = remove_image_status(kyobo_list)
    aladin_clean = remove_image_status(aladin_list)

    # DataFrame 생성
    df_yes24 = pd.DataFrame(yes24_clean)
    df_kyobo = pd.DataFrame(kyobo_clean)
    df_aladin = pd.DataFrame(aladin_clean)

    # 엑셀 파일로 저장
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df_yes24.to_excel(writer, sheet_name='YES24', index=False)
        df_kyobo.to_excel(writer, sheet_name='교보문고', index=False)
        df_aladin.to_excel(writer, sheet_name='알라딘', index=False)

    print(f"엑셀 파일 저장 완료: {filename}")
    return filename

# 메인 실행 함수
# ----------------------------------------
def crawl_start(keyword, yes24_pages=1, kyobo_pages=1, aladin_pages=1):
    """
    크롤링을 시작하는 메인 함수
    """
    print(f"크롤링 시작: '{keyword}' 검색")
    print(f"YES24: {yes24_pages}페이지, 교보문고: {kyobo_pages}페이지, 알라딘: {aladin_pages}페이지")
    
    try:
        yes24_list, kyobo_list, aladin_list = crawl_all(keyword, yes24_pages, kyobo_pages, aladin_pages)
        
        # 결과 출력
        print(f"\n=== 크롤링 결과 ===")
        print(f"YES24: {len(yes24_list)}개 항목")
        print(f"교보문고: {len(kyobo_list)}개 항목")
        print(f"알라딘: {len(aladin_list)}개 항목")
        
        # 엑셀 저장
        filename = save_to_excel(yes24_list, kyobo_list, aladin_list, keyword)
        
        return yes24_list, kyobo_list, aladin_list, filename
        
    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")
        return [], [], [], None

# ----------------------------------------
# 실행 예시
# ----------------------------------------
if __name__ == '__main__':
    keyword = '파이썬'
    yes24_list, kyobo_list, aladin_list, filename = crawl_start(keyword, 3, 5, 4)

    if filename:
        print(f"\n엑셀 파일이 성공적으로 저장되었습니다: {filename}")
    else:
        print("\n엑셀 파일 저장에 실패했습니다.")