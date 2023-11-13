def solution(s):
    result=[]
    for i in s.split(' '):
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)        
            
 