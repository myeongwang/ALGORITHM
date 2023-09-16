def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    quotient = s // n
    remainder = s % n
         
    if n == 2 and quotient * 2 + remainder == s:    
        answer = [quotient, remainder + quotient] 
    else:
        if remainder == 0:
            answer = [quotient] * n
        else:
            if remainder >= 1:
                answer = [quotient] * (n - remainder) + [quotient + 1] * remainder
                  
    return answer
        
        
    
    
    
    
    
