def solution(participant, completion):
    
    participant_dict = {} # 동명이인을 처리하기 위한 딕셔너리를 생성
    
    # 참가자 목록을 딕셔너리에 추가
    for part in participant:
        if part not in participant_dict:
            participant_dict[part] = 1
        else:
            participant_dict[part] += 1
    
    # 완주자 목록을 딕셔너리에서 빼기
    for com in completion:
        if com in participant_dict:
            participant_dict[com] -= 1
            if participant_dict[com] == 0:
                del participant_dict[com]  # 딕셔너리에서 완주한 참가자 삭제
                                           # del은 index의 요소 삭제
    return(list(participant_dict)[0])      # remove는 값을 삭제
    
    
"""
    participant_dict = {}  # 참가자를 딕셔너리로 변환
    
    for p in participant: #리스트 순회하며 딕셔너리에 추가, 이미 있는 경우 등장회수 증가
        if p in participant_dict:
            participant_dict[p] += 1 #증가
        else:
            participant_dict[p] = 1 #추가
    
        
    for c in completion: # 리스트 순회하며 완주한 선수 제거, 등장횟수 감소
        if c in participant_dict:
            participant_dict[c] -= 1 #감소
            if participant_dict[c] == 0:
                del participant_dict[c] #제거
    
   
    return list(participant_dict.keys())[0]
"""



