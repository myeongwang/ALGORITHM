def solution(price, money, count):
    total = sum(price * (i + 1) for i in range(count))
    
    if total <= money:
        return 0
    else:
        return total - money



    
    
    