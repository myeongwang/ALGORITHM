def solution(n, wires):
    def dfs(node, parent):
        # 해당 노드의 자식 노드들의 송전탑 개수를 구함
        sub_tree_sizes = [dfs(child, node) for child in graph[node] if child != parent]
        # 현재 노드를 포함한 서브 트리의 송전탑 개수
        total_size = 1 + sum(sub_tree_sizes)
        # 두 서브 네트워크의 송전탑 개수 차이를 계산하고 최소 차이 업데이트
        min_diff[0] = min(min_diff[0], abs(n - total_size * 2))
        return total_size
    
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    min_diff = [n]  # 최소 차이를 저장할 변수
    
    # 아무 노드에서 시작해도 됨. 여기서는 1번 노드에서 시작
    dfs(1, 0)
    
    return min_diff[0]
