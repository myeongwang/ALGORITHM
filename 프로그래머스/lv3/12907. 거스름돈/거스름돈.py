"""
def solution(n, money):
    total= [sum(i for i in money)]

    for i in range(len(money)):
        if money[i]>=n:
            if money[i]>n:
                money=[j for j in range(money-j) ]
            elif money[i]==n:
                money=[j for j in money]
                """

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    
    return dp[n] % 1000000007