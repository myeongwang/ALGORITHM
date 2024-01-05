def count_pairs(n, m):
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a * b) == 0:
                count += 1
    return count

t = int(input())  # 테스트 케이스 개수 입력

for _ in range(t):
    n, m = map(int, input().split())  # n과 m 입력
    result = count_pairs(n, m)
    print(result)
