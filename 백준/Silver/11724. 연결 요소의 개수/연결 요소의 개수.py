import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
hdc = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(v):
    visited[v]=True
    for i in hdc[v]:
        if not visited[i]:
            dfs(i)


for _ in range(m):
    s,e = map(int,input().split())
    hdc[s].append(e)
    hdc[e].append(s)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        count+=1
        dfs(i)
print(count)    
    
    
    