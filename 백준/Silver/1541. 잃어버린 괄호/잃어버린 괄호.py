import sys 
input = sys.stdin.readline
answer = 0
arr = list(map(str, input().split("-")))

def mysum(i):
    sum=0
    temp = str(i).split("+")
    for i in temp:
        sum+= int(i)
    return sum    
    
    
    
for i in range(len(arr)):
    if i==0:
        answer += mysum(arr[i])
    else:
        answer-= mysum(arr[i])
        
print(answer)        