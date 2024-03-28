from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 출발 지점부터의 거리를 저장할 배열
    distances = [[-1] * m for _ in range(n)]
    distances[0][0] = 1  # 출발 지점은 거리 1
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0)])
    
    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 다음 위치가 맵 범위 내에 있고, 이동할 수 있는 곳인 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and distances[nx][ny] == -1:
                # 다음 위치의 거리는 현재 위치의 거리 + 1
                distances[nx][ny] = distances[x][y] + 1
                # 다음 위치를 큐에 추가하여 탐색 계속
                queue.append((nx, ny))
    
    # 도착 지점의 거리 반환
    return distances[n-1][m-1]
