n = int(input())
arr = list(map(int, input().split()))

max_sum = [0] * n
max_sum[0] = arr[0]

for i in range(1, n):
    max_sum[i] = max(arr[i], max_sum[i-1] + arr[i])


print(max(max_sum))
