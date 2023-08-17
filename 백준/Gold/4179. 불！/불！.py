import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

# 입력 받은 미로를 2차원 리스트로 저장
for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque([(0, i, graph[i].index('J'))])  # 지훈이의 위치를 큐에 추가

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((-1, i, j))  # 불의 위치를 큐에 추가

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 dx, dy 값
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()

    # 지훈이 탈출 조건
    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
        ans = time + 1  # 시간 업데이트
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':

            # 지훈이 이동
            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                q.append((time + 1, nx, ny))

            # 불 퍼뜨리기
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)  # 결과 출력