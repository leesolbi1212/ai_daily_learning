# (1) 기본 예제 - 팩토리얼 계산
def factorial(n):
    if n == 1:
        return 1  # 종료 조건(Base Case)
    return n * factorial(n - 1)  # 재귀 호출

print(factorial(5))  # 결과: 120


# 중급 예제 - 피보나치 수열 계산 (“바로 앞 숫자” + “그 앞 숫자” = 새 숫자)
# **메모이제이션(memoization)**을 활용하여 성능을 향상시킨 예제.
# 이전 결과를 딕셔너리에 저장해서 중복 계산을 피함. 

memo = {}  # 중복 계산 방지를 위한 딕셔너리

def fibonacci(n):
    if n in (1, 2):
        return 1  # 종료 조건(Base Case)
    if n in memo:
        return memo[n]  # 이미 계산한 값 사용

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)  # 재귀 호출
    return memo[n]

print(fibonacci(10))  # 결과: 55