import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 각 구간의 합을 저장하는 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 구간 합 계산 및 출력
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = prefix_sum[j] - prefix_sum[i - 1]
    print(result)


    
    


