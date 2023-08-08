#boj 15649 N과 M

def backtracking(N, M, selected, visited):
    if len(selected) == M:
        print(' '.join(map(str, selected)))  # 선택된 수를 공백으로 구분하여 출력
        return

    for num in range(1, N + 1):
        if not visited[num]:
            visited[num] = True
            selected.append(num)
            backtracking(N, M, selected, visited) #결국 백트래킹도 재귀?
            visited[num] = False
            selected.pop()

N, M = map(int, input().split())
visited = [False] * (N + 1)  # 각 숫자의 방문 여부를 체크하는 리스트
backtracking(N, M, [], visited)