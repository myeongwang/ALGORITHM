n= int(input())
finds = list(map(int,input().split()))
m= int(input())
arr = list(map(int,input().split()))

finds.sort()

def solution(value,start,end):
    low,high = start,end
    while low<=high:
        mid = (low+high)//2
        if finds[mid] < value:
            low = mid+1
        elif finds[mid] > value:
            high =mid-1
        else:
            return True
    return False

for find in arr:
    if solution(find,0,n-1):
        print(1)
    else:
        print(0)
