import sys
input = sys.stdin.readline

m= int(input())
n=int(input())
arr = list(map(int,input().split()))
arr.sort()

count =0
i=0
j=m-1

while i<j:
    if arr[i]+arr[j]>n:
        j-=1
    elif arr[i]+arr[j]<n:
        i+=1
        
    else:
        count+=1
        i+=1
        j-=1
print(count)    
    
    
    