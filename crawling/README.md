# 도서 크롤링 프로그램

셀레니움을 이용하여 YES24, 교보문고, 알라딘에서 도서 정보를 크롤링하고 엑셀로 저장하는 프로그램입니다.

## 기능

- **YES24**: 도서 검색 및 정보 크롤링
- **교보문고**: 도서 검색 및 정보 크롤링  
- **알라딘**: 도서 검색 및 정보 크롤링
- **이미지 다운로드**: 각 사이트별로 이미지 파일 저장
- **엑셀 저장**: 사이트별로 시트를 분리하여 저장

## 크롤링 정보

각 도서에 대해 다음 정보를 수집합니다:
- 검색어
- 책제목
- 저자
- 가격
- 출판사
- 출판일
- 이미지 경로

## 설치 및 실행

### 1. 필요한 패키지 설치

```bash
pip install selenium requests openpyxl pandas
```

### 2. Chrome WebDriver 설치

Chrome 브라우저가 설치되어 있어야 합니다.

### 3. 프로그램 실행

```python
from bookCrawler import crawl_start

# 기본 사용법 (각 사이트 1페이지씩)
crawl_start('파이썬')

# 페이지 수 지정
crawl_start('파이썬', yes24_pages=3, kyobo_pages=5, aladin_pages=4)
```

## 사용 예시

### 기본 크롤링
```python
# 각 사이트 1페이지씩 크롤링
yes24_list, kyobo_list, aladin_list, filename = crawl_start('파이썬')
```

### 페이지 수 지정
```python
# YES24 2페이지, 교보문고 3페이지, 알라딘 2페이지
yes24_list, kyobo_list, aladin_list, filename = crawl_start('파이썬', 2, 3, 2)
```

### 직접 실행
```bash
python bookCrawler.py
```

## 출력 결과

### 1. 이미지 파일
- `images/yes24/`: YES24 도서 이미지
- `images/kyobo/`: 교보문고 도서 이미지  
- `images/aladin/`: 알라딘 도서 이미지

### 2. 엑셀 파일
- `{검색어}_books.xlsx`: 크롤링 결과
- 시트: YES24, 교보문고, 알라딘

## 프로그램 구조

```
bookCrawler.py          # 메인 크롤링 프로그램
test_crawler.py         # 테스트 스크립트
images/                 # 이미지 저장 폴더
├── yes24/             # YES24 이미지
├── kyobo/             # 교보문고 이미지
└── aladin/            # 알라딘 이미지
```

## 주요 함수

### `crawl_start(keyword, yes24_pages=1, kyobo_pages=1, aladin_pages=1)`
크롤링을 시작하는 메인 함수

**매개변수:**
- `keyword`: 검색할 키워드
- `yes24_pages`: YES24 크롤링할 페이지 수
- `kyobo_pages`: 교보문고 크롤링할 페이지 수  
- `aladin_pages`: 알라딘 크롤링할 페이지 수

**반환값:**
- `yes24_list`: YES24 크롤링 결과 리스트
- `kyobo_list`: 교보문고 크롤링 결과 리스트
- `aladin_list`: 알라딘 크롤링 결과 리스트
- `filename`: 생성된 엑셀 파일명

## 오류 처리

- 검색 결과가 없으면 빈 리스트 반환
- 이미지 다운로드 실패 시 오류 메시지 기록
- 페이지네이션 오류 시 현재 페이지에서 중단

## 주의사항

1. 웹사이트 구조 변경 시 셀렉터 업데이트 필요
2. 과도한 크롤링은 서버에 부하를 줄 수 있음
3. 이미지 파일명은 책제목 기반으로 생성됨
4. 네트워크 상태에 따라 일부 이미지 다운로드 실패 가능

## 테스트

```bash
python test_crawler.py
```

## 라이선스

이 프로그램은 교육 목적으로 제작되었습니다. 