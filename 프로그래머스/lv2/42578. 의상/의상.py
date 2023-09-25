def solution(clothes):
    clothes_type = {}

    for _, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 1
        else:
            clothes_type[t] += 1
            
    answer = 1
    
    # 각 옷 종류별로 (개수 + 1)을 곱해줌
    for cnt in clothes_type.values():
        answer *= (cnt + 1)
    
    # 모든 종류를 입지 않는 경우는 제외
    answer -= 1
    
    return answer
    