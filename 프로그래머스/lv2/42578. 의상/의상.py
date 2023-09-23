def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
            
    print(clothes_type)
    cnt = 1
    for num in clothes_type.values():
        cnt *= num
    print(clothes_type.values())
    return cnt - 1