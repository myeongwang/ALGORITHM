def solution(participant, completion):
    
    participant_dict={}
    
    for p in participant:
        if p in participant_dict:
            participant_dict[p]+=1 #이미 있는 경우(동명이인)
        else:
            participant_dict[p]=1
            
    for c in completion:
        if c in participant_dict:
            participant_dict[c]-=1
            if participant_dict[c]==0:
                del participant_dict[c]
                
    return list(participant_dict.keys())[0]
    
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



