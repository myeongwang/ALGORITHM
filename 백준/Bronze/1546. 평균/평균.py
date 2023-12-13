n = int(input())
numbers = list(map(int, input().split()))  
numbers.sort()
arr = []

for i in range(n):
    a = numbers[n-1]  
    arr.append(numbers[i] / a * 100)

average = sum(arr) / n
print(average)

    
    