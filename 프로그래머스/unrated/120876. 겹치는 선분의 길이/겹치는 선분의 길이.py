def solution(lines):
    line=[ 0 for i in range(200)]
    
    for a,b in lines:
        while a<b:
            line[a+100]+=1
            a+=1
    return len(list(filter(lambda x:x>1,line)))        
    