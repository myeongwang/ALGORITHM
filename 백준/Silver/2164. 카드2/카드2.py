from collections import deque

n= int(input())
myqueue = deque()

for i in range(1,n+1):
    myqueue.append(i)
    
while len(myqueue)>1:
    myqueue.popleft()
    myqueue.append(myqueue.popleft())
    
print(myqueue[0])    

