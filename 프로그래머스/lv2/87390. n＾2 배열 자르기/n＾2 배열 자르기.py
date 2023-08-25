def solution(n, left, right):
    
    arr=[]
    
    #return [max(i//n+1, i%n+1) for i in range(left, right+1)]
    for i in range(left,right+1):
        arr.append(max(i//n+1, i%n+1))
    return arr    