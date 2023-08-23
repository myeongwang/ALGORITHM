def solution(price, money, count):
    arr = []
    
    for i in range(2, count + 1):
        arr.append(i * price)        
        
    total= sum(arr)-money+price  # arr_1 리스트의 모든 값의 합 계산
    
    if total<=0:
        return 0
    
    return total



    
    
    