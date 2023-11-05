def solution(s):
    dic={}
    
    for char in s:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1
    #print(sorted([char for char, count in dic.items() if count ==1 ]))        
    return ''.join(sorted([char for char, count in dic.items() if count ==1 ]))
    
    