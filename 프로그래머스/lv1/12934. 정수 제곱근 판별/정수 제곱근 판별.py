import math

def solution(n):
    # n의 제곱근을 계산
    sqrt_n = int(math.sqrt(n))
    
    # 제곱근을 다시 제곱하여 n과 비교
    if sqrt_n * sqrt_n == n:
        return (sqrt_n + 1) *(sqrt_n+1)
    else:
        return -1