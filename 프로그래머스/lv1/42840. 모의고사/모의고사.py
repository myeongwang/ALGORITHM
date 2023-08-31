def solution(answers):
    pattern1=[1,2,3,4,5]
    pattern2=[2,1,2,3,2,4,2,5]
    pattern3=[3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    result=[]
    
    
   # 정답 배열과 각 수포자의 패턴을 비교하여 점수 계산
    for i, ans in enumerate(answers):
        if ans == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if ans == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if ans == pattern3[i % len(pattern3)]:
            scores[2] += 1
    max_score=max(scores)
    #천재다 이건
    
    for i in range(len(scores)):
        if scores[i]== max(scores):
            result.append(i+1)
        
    return result