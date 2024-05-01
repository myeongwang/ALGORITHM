N = int(input())
for i in range(N):
    M = int(input())
    answer = 0
    arr = list(map(int, input().split()))
    sellPrice = 0

    for val in arr[::-1]:
        if val >= sellPrice:
            sellPrice = val
        else:
            answer += sellPrice - val
    print("#", i + 1, " ", answer, sep="")