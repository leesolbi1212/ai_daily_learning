# 탑다운 방식을 이용한 피보나치 수열

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 
memo = [0] * 100 # 크기를 미리 정해주기, 인덱스 접근이 빠르고 간단함. 
# 만약 memo = {} 딕셔너리로 한다면 필요한 만큼 메모리를 쓰고, n 범위에 제약 없음. 

# 피보나치 수열을 재귀함수로 구현(topdown)
def fibo(x):
  # fibo(1)=fibo(2)=0
  if x==1 or x==2:
    return 1

  # 이미 계산한 적있는 문제라면 그대로 반환
  if memo[x] != 0:
    return memo[x]

  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  memo[x] = fibo(x-1)+fibo(x-2)
  return memo[x]


print(fibo(99))

# 피보나치 수열을 반복문으로 구현(bottom up)
for i in range(3, n+1):
  dp[i] = dp[i-1]+dp[i-2]

print(dp[n])