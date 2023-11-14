"""
def solution(n):
    answer =0
    for _ in range(n):
        answer+=1
        while '3' in str(n) or n %3==0:
            answer+=1
    return answer
"""


def solution(n):
    answer=[i for i in range(1,1001) if i%3!=0 and not ('3' in str(i))]
    
    return answer[n-1]
       
            