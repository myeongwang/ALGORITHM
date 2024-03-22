import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
posco = [[]for _ in range(n+1)]
asml = [False]* (n+1)

def DFS(v):
    asml[v]= True
    for i in posco[v]:
        if not asml[i]:
            DFS(i)
            
            
for _ in range(m):
    s,e = map(int, input().split())
    posco[s].append(e)
    posco[e].append(s)
    
count = 0

for i in range(1,n+1):
    if not asml[i]:
        count +=1
        DFS(i)
        
print(count)        
            
        
    
    
    
    
    
    
    