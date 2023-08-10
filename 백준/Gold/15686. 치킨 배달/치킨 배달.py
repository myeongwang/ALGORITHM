from sys import maxsize

def chicken_distance(home, selected_chickens):
    total_distance = 0
    
    for hx, hy in home:
        min_distance = maxsize
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    
    return total_distance

def dfs(idx, selected_chickens):
    global min_total_distance
    
    if len(selected_chickens) == M:
        total_distance = chicken_distance(home, selected_chickens)
        min_total_distance = min(min_total_distance, total_distance)
        return
    
    for i in range(idx, len(chickens)):
        selected_chickens.append(chickens[i])
        dfs(i + 1, selected_chickens)
        selected_chickens.pop()

N, M = map(int, input().split())
arr = []

home = []
chickens = []

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

min_total_distance = maxsize
dfs(0, [])
print(min_total_distance)