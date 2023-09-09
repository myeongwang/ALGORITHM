def solution(price, money, count):
    total = [ price*i for i in range(1,count+1)]
    total_sum=0
    
    for i in range(count):
        total_sum+=total[i]
    
    if total_sum-money>0:
        return total_sum - money
    else:
        return 0


    
    
    