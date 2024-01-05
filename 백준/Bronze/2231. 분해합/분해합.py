N = int(input())  
for num in range(1, N+1):
    arrs = [int(arr) for arr in str(num)]  
    num_sum = num + sum(arrs)  

    if num_sum == N:  
        print(num) 
        break  

if num == N: 
    print(0)  
