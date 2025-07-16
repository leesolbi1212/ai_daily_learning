import time
import os
import urllib.request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient

# 설정 
keyword   = "cat"
save_dir  = r"C:\AI_SW\crawling\images"
max_pages = 10

# MongoDB 연결
MONGO_URI = (
    "mongodb+srv://apple:7HEjkdBrMut8Ni0R@cluster0.y9fb3fs.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Cluster0"
)
client     = MongoClient(MONGO_URI)
collection = client["imgcrawring"]["cat"]

# 저장 폴더 생성
os.makedirs(save_dir, exist_ok=True)

# 브라우저 실행 & 최초 페이지 접속 
driver = webdriver.Chrome()
driver.get(f"https://pixabay.com/images/search/{keyword}/")
time.sleep(2)

page = 1
while page <= max_pages:
    print(f"\n▶ {page}페이지 크롤링 중…")

    # 1) 전체 페이지 스크롤로 기본 이미지 로드
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(1)

    # 2) 모든 셀 요소 수집
    cells = driver.find_elements("css selector", "div.cell--UMz-x")
    print("  • 찾은 셀 개수:", len(cells))

    # 3) lazy-load 트리거: 각 셀을 스크롤해서 실제 이미지 로드
    for cell in cells:
        driver.execute_script("arguments[0].scrollIntoView(true);", cell)
        time.sleep(0.1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # 4) 이미지 URL 추출
    img_urls = []
    for cell in cells:
        try:
            img = cell.find_element("tag name", "img")
            src = img.get_attribute("src")
            if src and src.startswith("https"):
                img_urls.append(src)
        except:
            continue
    print("  • 유효 URL 개수:", len(img_urls))

    # 5) 다운로드 및 MongoDB 저장
    for idx, url in enumerate(img_urls, start=1):
        ext      = os.path.splitext(url)[1].split("?")[0] or ".jpg"
        filename = f"{keyword}_{page}_{idx}{ext}"
        fpath    = os.path.join(save_dir, filename)

        try:
            req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp, open(fpath, "wb") as out:
                out.write(resp.read())
            print("   ↓ 저장 완료:", filename)

            doc = {
                "keyword":    keyword,
                "page":       page,
                "index":      idx,
                "image_url":  url,
                "local_path": fpath.replace("\\", "/"),
                "timestamp":  time.time()
            }
            collection.insert_one(doc)

        except Exception as e:
            print("   ! 저장 실패:", e)

    # 6) 다음 페이지로 이동
    try:
        next_btn = driver.find_element("css selector", "a[rel='next']")
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)
        page += 1
    except (NoSuchElementException, ElementClickInterceptedException):
        print("다음 페이지 없음, 크롤링 종료.")
        break

driver.quit()
print("전체 크롤링 및 저장 완료!")
