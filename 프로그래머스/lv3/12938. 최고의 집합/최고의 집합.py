def solution(n, s):
    if n > s:
        return [-1]
    
    quotient = s // n
    remainder = s % n
    
    answer = [quotient] * n
    
    for i in range(remainder):
        answer[-(i + 1)] += 1
    
    return answer