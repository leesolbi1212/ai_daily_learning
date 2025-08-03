#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
도서 크롤링 프로그램 테스트 스크립트
"""

from bookCrawler import crawl_start

def main():
    print("=== 도서 크롤링 프로그램 테스트 ===")
    print()
    
    # 테스트 1: 기본 크롤링 (각 사이트 1페이지씩)
    print("1. 기본 크롤링 테스트 (각 사이트 1페이지씩)")
    keyword = "파이썬"
    yes24_list, kyobo_list, aladin_list, filename = crawl_start(keyword, 1, 1, 1)
    
    print(f"\n결과:")
    print(f"- YES24: {len(yes24_list)}개 항목")
    print(f"- 교보문고: {len(kyobo_list)}개 항목") 
    print(f"- 알라딘: {len(aladin_list)}개 항목")
    print(f"- 엑셀 파일: {filename}")
    
    print("\n" + "="*50)
    
    # 테스트 2: 다른 검색어로 테스트
    print("2. 다른 검색어 테스트")
    keyword2 = "자바"
    yes24_list2, kyobo_list2, aladin_list2, filename2 = crawl_start(keyword2, 1, 1, 1)
    
    print(f"\n결과:")
    print(f"- YES24: {len(yes24_list2)}개 항목")
    print(f"- 교보문고: {len(kyobo_list2)}개 항목")
    print(f"- 알라딘: {len(aladin_list2)}개 항목")
    print(f"- 엑셀 파일: {filename2}")
    
    print("\n" + "="*50)
    
    # 사용법 안내
    print("3. 사용법 안내")
    print("""
크롤링 프로그램 사용법:
    
# 기본 사용법 (각 사이트 1페이지씩)
crawl_start('검색어')

# 페이지 수 지정
crawl_start('검색어', yes24_pages=3, kyobo_pages=5, aladin_pages=4)

# 예시
crawl_start('파이썬', 2, 3, 2)  # YES24 2페이지, 교보문고 3페이지, 알라딘 2페이지

결과:
- 각 사이트별로 이미지가 images/폴더에 저장됩니다
- 엑셀 파일이 생성되며 각 사이트별로 시트가 분리됩니다
- 검색 결과가 없으면 정상적으로 빈 리스트를 반환합니다
    """)

if __name__ == "__main__":
    main() 