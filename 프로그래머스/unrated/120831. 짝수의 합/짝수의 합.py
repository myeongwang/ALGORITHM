def solution(n):
    arr = []
    total = 0
    
    for i in range(2, n+1, 2):  # Directly iterate over even numbers
        arr.append(i)
   
    for j in arr:
        total += j  # Correct the addition operation
        print(total)
    return total

        
        
        