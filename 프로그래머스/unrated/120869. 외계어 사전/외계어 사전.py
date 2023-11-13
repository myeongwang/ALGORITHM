def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s): #spell 문자열의 집합에서 s 문자열의 집합을 빼고 결과 집합이 비어있는지 확인
            return 1
    return 2

"""
def solution(spell, dic):
    
    for d in dic:
        if sorted(d)==sorted(spell):
            return 1
    return 2    
    
    """