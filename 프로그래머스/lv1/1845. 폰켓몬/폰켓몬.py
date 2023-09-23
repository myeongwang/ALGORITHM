def solution(nums):
    # 해시맵을 사용하여 각 폰켓몬 종류의 개수를 저장
    pokemon_count = {}
    
    for num in nums:
        if num in pokemon_count:
            pokemon_count[num] += 1
        else:
            pokemon_count[num] = 1
    print(pokemon_count)
    print(len(pokemon_count))
    # 최대 종류의 개수를 계산
    max_kinds = min(len(nums) // 2, len(pokemon_count))
    
    return max_kinds