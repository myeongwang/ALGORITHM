def solution(a):
    answer =2
    
    if len(a)<=2:
        return len(a)
    
    left_min=a[0]
    right_min=a[-1]
    
    left_checked=[0]*len(a)
    right_checked=[0]*len(a)
    
    for i in range(1,len(a)-1):
        if a[i]< left_min:
            left_min = a[i]
            left_checked[i]=1
            
        if a[-i-1]< right_min:
            right_min = a[-i-1]
            right_checked[-i-1]=1
            
    for i in range(len(a)):
        if left_checked[i] or right_checked[i]: 
            answer+=1                               
    return answer     
        
        