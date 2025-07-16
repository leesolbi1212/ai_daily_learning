from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, os, time
from pymongo import MongoClient

# ─── 설정 ─────────────────────────────────────────────────────────────
QUERY      = "cat"
MAX_PAGES  = 10
SAVE_DIR   = r"C:\AI_SW\crawling\images"
CHROMEDRIVER_PATH = r"C:\tools\chromedriver.exe"  # 실제 chromedriver.exe 경로
MONGO_URI  = "mongodb+srv://apple:7HEjkdBrMut8Ni0R@cluster0.y9fb3fs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME    = "imgcrawring"
COL_NAME   = "cat"

os.makedirs(SAVE_DIR, exist_ok=True)
client = MongoClient(MONGO_URI)
col    = client[DB_NAME][COL_NAME]

# ─── WebDriver 준비 ───────────────────────────────────────────────────
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")   # ← 디버깅할 땐 주석 처리!
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)
wait   = WebDriverWait(driver, 10)

# ─── 크롤링 루프 ───────────────────────────────────────────────────────
# **올바른** 검색 URL
base_url = f"https://pixabay.com/images/search/{QUERY}/"
driver.get(base_url)

for page in range(1, MAX_PAGES + 1):
    print(f"[Page {page}] 크롤링…")
    container = wait.until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[3]'
    )))
    groups = container.find_elements(By.XPATH, "./div")
    
    for grp in groups[1:]:  # 0번째는 Sponsored
        for a in grp.find_elements(By.TAG_NAME, "a"):
            try:
                img = a.find_element(By.TAG_NAME, "img")
                src = img.get_attribute("src")
                if not src:
                    continue

                fname = f"{QUERY}_p{page}_{os.path.basename(src)}"
                fpath = os.path.join(SAVE_DIR, fname)

                resp = requests.get(src, timeout=10)
                with open(fpath, "wb") as f:
                    f.write(resp.content)

                col.insert_one({
                    "url": src,
                    "path": fpath,
                    "page": page,
                    "timestamp": time.time()
                })
                print("   ↓", fname)

            except Exception as e:
                print("   !", e)

    # 다음 페이지
    try:
        nxt = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@rel="next"]')))
        nxt.click()
        time.sleep(2)
    except:
        print("다음 페이지 없음, 종료.")
        break

driver.quit()
print("크롤링 완료.")
