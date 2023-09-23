def solution(nums):
    pockemon_dict={}
    
    for n in nums:
        if n not in pockemon_dict:
            pockemon_dict[n]=1
        else:
            pockemon_dict[n]+=1
  
            
    return min(len(nums)/2 , len(pockemon_dict) )       


# 아래의 set 이용하면 해시의 len 사용할 필요없이 바로 중복 제거
"""

def solution(nums):
    # N/2 마리의 폰켓몬을 선택해야 하므로 선택할 수 있는 최대 종류의 개수는 N/2입니다.
    max_kinds = len(nums) // 2
    
    # 폰켓몬 종류 번호를 set으로 변환하여 중복을 제거합니다.
    unique_pokemons = set(nums)
    
    # 중복을 제거한 폰켓몬 종류 수와 최대 종류 수 중 작은 값을 반환합니다.
    return min(max_kinds, len(unique_pokemons)) """
