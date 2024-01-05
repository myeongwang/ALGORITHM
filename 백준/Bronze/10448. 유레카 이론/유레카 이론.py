def find_eureka(k):
    for i in range(1, 45):
        for j in range(1, 45):
            for m in range(1, 45):
                if i * (i + 1) // 2 + j * (j + 1) // 2 + m * (m + 1) // 2 == k:
                    return True
    return False

n = int(input())
for _ in range(n):
    k = int(input())
    if find_eureka(k):
        print(1)
    else:
        print(0)
