def solution(score):
    answer = []
   
    
    for i in range(len(score)):
        answer.append((score[i][0]+score[i][1])/2)
    

    return [sorted(answer,reverse=True).index(num)+1 for num in answer]