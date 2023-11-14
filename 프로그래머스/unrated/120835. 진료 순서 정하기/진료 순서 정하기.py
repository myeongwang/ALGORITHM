def solution(emergency):
    dic = {}
    
    for char in emergency:
        dic[char] = sorted(emergency, reverse=True).index(char) + 1
        
     
    return [dic[char]for char in emergency] #[]처리가 ㅈㄴ 중요함

        
   