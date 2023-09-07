dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
dy = {'N': 0, 'S':0, 'E':1, 'W':-1}

def solution(park, routes):
    answer = []
    x, y = -1, -1
    N, M = len(park), len(park[0])
    for i in range(N): #find location
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        dir_, dist = route.split(' ')

        isFalse = False
        for i in range(1, int(dist) + 1):
            nx, ny = x + dx[dir_] * i, y + dy[dir_] * i
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1: #위치를 벗어나거나
                isFalse = True
                break
            if park[nx][ny] == 'X': #장애물이 있거나
                isFalse = True
                break

        if isFalse:
            continue
        nx, ny = x + dx[dir_] * int(dist), y + dy[dir_] * int(dist)
        x, y = nx, ny

    answer = [x, y]

    return answer