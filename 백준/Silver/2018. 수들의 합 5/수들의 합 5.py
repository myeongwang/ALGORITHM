import sys
input = sys.stdin.readline

n = int(input())

count = 0
for i in range(1, n+1):
    s = i * (i + 1) // 2  # 1부터 i까지의 합을 계산하는 공식
    if s > n:
        break
    if (n - s) % i == 0:  # n에서 1부터 i까지의 합을 뺀 값이 i의 배수인지 확인
        count += 1

print(count)
