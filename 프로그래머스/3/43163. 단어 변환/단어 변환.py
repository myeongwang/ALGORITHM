from collections import deque

def can_convert(word1, word2):
    # 두 단어간에 한 글자만 다른지 확인
    diff_count = sum(1 for x, y in zip(word1, word2) if x != y)
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set()  # 방문한 단어를 기록
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_convert(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
    
    return 0
