def solution(order):
    order = list(str(order))
    count=0
    
    for i in order:
        if i == '3' or i == '6' or i == '9':
            count += 1
            
    return count

           