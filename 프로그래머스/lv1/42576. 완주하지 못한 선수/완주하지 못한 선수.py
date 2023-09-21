def solution(participant, completion):
    participant_dict = {}  # 참가자를 딕셔너리로 변환
    
    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    
    for c in completion:
        if c in participant_dict:
            participant_dict[c] -= 1
            if participant_dict[c] == 0:
                del participant_dict[c]
    
    answer = list(participant_dict.keys())[0]
    return answer
