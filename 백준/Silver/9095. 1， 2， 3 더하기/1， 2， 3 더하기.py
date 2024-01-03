def count_ways_to_sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return count_ways_to_sum(n - 1) + count_ways_to_sum(n - 2) + count_ways_to_sum(n - 3)

t = int(input())  # 테스트 케이스 수 입력

for _ in range(t):
    n = int(input())  # 각 테스트 케이스에 대한 입력
    result = count_ways_to_sum(n)
    print(result)

    
    
