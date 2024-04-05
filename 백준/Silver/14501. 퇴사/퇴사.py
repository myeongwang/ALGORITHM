import sys

n = int(input())
consulting = []

for _ in range(n):
    t, p = map(int, input().split())
    consulting.append([t, p])

dp = [0] * (n + 1)  # dp[i]는 i번째 날까지의 최대 보수를 저장합니다.

for i in range(n - 1, -1, -1):
    next_day = i + consulting[i][0]
    
    # 현재 상담을 선택하지 않는 경우
    dp[i] = dp[i + 1]
    
    # 현재 상담을 선택하는 경우
    if next_day <= n:
        dp[i] = max(dp[i], consulting[i][1] + dp[next_day])

print(dp[0])

