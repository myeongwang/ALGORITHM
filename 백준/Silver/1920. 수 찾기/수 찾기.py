# 완전탐색 시 시간초과 

N = int(input().strip())
digits = list(map(int, input().split()))
M = int(input().strip())
finds = list(map(int, input().split()))

digits.sort()

def binary_search(value, start, end):
    low, high = start, end
    while low <= high:
        mid = (low + high) // 2
        if digits[mid] < value:
            low = mid + 1
        elif digits[mid] > value:
            high = mid - 1
        else:
            return True
    return False
    

for find in finds:
    if binary_search(find, 0, N - 1):
        print (1)
    else:
        print (0)
