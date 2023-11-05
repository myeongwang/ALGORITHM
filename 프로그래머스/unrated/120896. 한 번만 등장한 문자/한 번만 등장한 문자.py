#3.
from collections import Counter

def solution(s):
    string = []
    for i,j in Counter(s).items():
        if j ==1:
            string.append(i)
    return ''.join(sorted(string))        
    
"""
#1
def solution(s):
    return ''.join(sorted([c for c in s if s.count(c)==1]))
    
#2
def solution(s):
    dic={}
    
    for char in s:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1
    #print(sorted([char for char, count in dic.items() if count ==1 ]))        
    return ''.join(sorted([char for char, count in dic.items() if count ==1 ]))
    #.items: 딕셔너리 값 반환 
"""    
