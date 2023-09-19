"""
from itertools import permutations

def solution(n, k):
    numbers = list(range(1, n + 1))
    perms = list(permutations(numbers))

    answer = perms[k - 1]
    return answer
    """
"""

import math

def solution(n, k):
    numbers = list(range(1, n + 1))
    answer = []

    k -= 1  # k는 0부터 시작하도록 조정
    for i in range(n):
        # n-1개의 숫자 중에서 각각의 숫자가 몇 번째로 오는지 계산
        index = k // math.factorial(n - 1 - i)
        answer.append(numbers.pop(index))
        k %= math.factorial(n - 1 - i)

    return answer
"""
from math import factorial

def solution(n, k):
   
    answer = []
    order = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        #answer.append(order.pop(k//fact-1 if k%fact ==0 else k//fact))
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact
    return answer
