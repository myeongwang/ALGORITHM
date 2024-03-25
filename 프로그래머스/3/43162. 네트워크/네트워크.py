def dfs(computers, visited, start):
    visited[start] = True
    for i in range(len(computers)):
        if computers[start][i] == 1 and not visited[i]:
            dfs(computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    return answer

# # 예시 입력
# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(n, computers))  # 출력: 2
