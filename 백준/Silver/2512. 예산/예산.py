import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()

low, high = 0, arr[-1]
while low <= high:
    mid = (low + high) // 2
    budget = sum(min(mid, a) for a in arr)
    
    if budget <= M:
        low = mid + 1
    else:
        high = mid - 1

print (high)