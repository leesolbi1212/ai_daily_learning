'''
※ xpath
XPath는 XML 또는 HTML 문서 내에서 특정 요소나 속성을 선택하기 위해 사용되는 경로 표현 언어입니다. 웹 크롤링이나 자동화 도구에서 주로 사용되며, 요소를 효율적으로 찾을 수 있도록 도와줍니다. 일반적인 XPath는 특정 위치나 속성을 기준으로 요소를 선택하는 상대적인 경로를 사용합니다. 또한 full xpath는 루트 요소에서 시작하여 대상 요소까지의 절대적인 경로를 나타냅니다. 따라서 문서 구조가 변경되면 경로가 깨질 가능성이 높습니다.
'''

전체
/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul

li 반복
# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul/li[1]
# li의 번호를 지우고 이 같은 형제(공통)를 다 뽑아보겠다!
/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul/li

p 태그 
# //*[@id="wcc_root"]/section/ul/li[2]/div[1]/div[2]/div/p
//*[@id="wcc_root"]/section/ul/li/div/div[2]/div/p