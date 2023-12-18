import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
temp =0

# 각 구간의 합을 저장하는 배열 생성
for i in arr:
    temp +=i
    prefix_sum.append(temp)
   
# 구간 합 계산 및 출력
for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    print(prefix_sum[e]-prefix_sum[s-1])
    
    


