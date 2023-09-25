def solution(s):
    answer=[]
    
    for char in s:
        if char =="(":
            answer.append(char)
        elif char ==")":
            if not answer:
                return False
            answer.pop()
    return len(answer)==0       
        
            
        
