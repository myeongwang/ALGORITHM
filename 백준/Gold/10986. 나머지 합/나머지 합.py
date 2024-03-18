from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 부분합 계산
prefix_sum = defaultdict(int)
prefix_sum[0] = 1
cur_sum = 0
count = 0

for num in arr:
    cur_sum = (cur_sum + num) % m
    count += prefix_sum[cur_sum]
    prefix_sum[cur_sum] += 1

print(count)
