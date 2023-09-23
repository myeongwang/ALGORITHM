def solution(clothes):
    # 각 의상 종류별로 개수를 저장할 딕셔너리 생성
    clothes_dict = {}
    
    # 의상 종류별로 개수를 카운트
    for _, category in clothes:
        if category in clothes_dict:
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1
    
    # 각 종류별로 선택할 수 있는 방법의 수 계산
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1)  # 해당 종류의 의상을 선택하지 않는 경우도 포함
    
    # 모든 종류의 조합 수에서 모두 선택하지 않는 경우(아무것도 입지 않는 경우)를 제외
    return combinations - 1
