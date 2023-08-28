def solution(a):
    answer = 2  # 처음과 끝의 풍선은 항상 남을 것이므로 2개부터 시작
    
    if len(a) <= 2:
        return len(a)
    
    left_min = a[0]  # 현재 위치까지의 최소값
    right_min = a[-1]  # 현재 위치부터 끝까지의 최소값
    
    left_checked = [0] * len(a)  # 왼쪽부터 풍선을 터트렸을 때 남는지 여부를 기록하는 리스트
    right_checked = [0] * len(a)  # 오른쪽부터 풍선을 터트렸을 때 남는지 여부를 기록하는 리스트
    
    for i in range(1, len(a) - 1):
        if a[i] < left_min:
            left_min = a[i]
            left_checked[i] = 1
            
        if a[-i - 1] < right_min:
            right_min = a[-i - 1]
            right_checked[-i - 1] = 1
    
    for i in range(len(a)):
        if left_checked[i] or right_checked[i]:
            answer += 1
    
    return answer











