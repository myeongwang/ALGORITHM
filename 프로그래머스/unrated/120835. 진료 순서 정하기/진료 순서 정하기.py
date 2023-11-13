def solution(emergency):
    dic={}
    
    for char in emergency:
        dic[char] = sorted(emergency,reverse=True).index(char)+1
     
        
    return [dic[num]for num in emergency]    
