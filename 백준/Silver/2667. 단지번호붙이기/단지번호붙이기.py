import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [] # 입력받을 그래프
result = [] # 결과 저장
count = 0 # 단지 내 집 갯수 

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
dx = [0, 0, 1, -1] # x축 정의 
dy = [1, -1, 0, 0] # y축 정의 

def dfs(x, y):
    global count

    if x < 0 or x >= n or y < 0 or y >= n: # n으로 수정
        return # 만약 좌표가 그래프의 범위를 벗어나면 함수를 종료

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()  # 오름차순으로 정렬

print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)
