def solution(array, n):
    total=0
    
    for i in array:
        if i==n:
            total+=1
    return total        