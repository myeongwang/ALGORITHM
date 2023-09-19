import math

def solution(brown, yellow):
    sum = brown + yellow
    
    for h in range(3,int(math.sqrt(sum))+1):
        if sum% h ==0:
            w= sum//h
            if (w-2)*(h-2) == yellow:
                return [w,h]
    
 