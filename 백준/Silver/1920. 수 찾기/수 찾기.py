import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    
    start = 0
    end = len(A) - 1
    
    while start <= end:
        mid = (start + end) // 2
        midv = A[mid]
        
        if midv > target:
            end = mid - 1
        elif midv < target:
            start = mid + 1
        else:
            find = True
            break
            
    if find:
        print(1)
    else:
        print(0)
