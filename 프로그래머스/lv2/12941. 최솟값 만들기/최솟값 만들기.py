def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    C=[]
    sum=0
    
    for i in range(len(A)):
        C.append(A[i]*B[i])
        sum+=C[i]
        
    return(sum)
    
    
    
    



