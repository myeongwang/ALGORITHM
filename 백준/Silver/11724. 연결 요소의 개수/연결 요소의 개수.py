import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]  # 인접 리스트 초기화
visited = [False] * (n + 1)  # 방문 리스트 초기화

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n + 1):
    if not visited[i]:  # 연결노드 중 방문하지 않았던 노드만 탐색
        count += 1
        DFS(i)

print(count)
