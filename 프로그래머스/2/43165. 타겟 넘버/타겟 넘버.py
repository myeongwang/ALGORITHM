def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer
        
        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            # 타겟 넘버와 일치하는지 확인하여 카운트
            if total == target:
                answer += 1
            return
        
        # 현재 숫자를 더하거나 빼는 모든 경우를 탐색
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    
    # DFS 실행
    dfs(0, 0)
    
    return answer

# # 예시 입력
# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target))  # 출력: 5
