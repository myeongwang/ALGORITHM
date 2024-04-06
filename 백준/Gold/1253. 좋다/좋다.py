n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 입력받은 수열을 오름차순으로 정렬합니다.

count = 0

for i in range(n):
    target = arr[i]  # 현재 검사하는 수를 target으로 설정합니다.
    start = 0
    end = n - 1
    
    while start < end:
        if start == i:  # 현재 검사하는 수는 건너뜁니다.
            start += 1
            continue
        
        if end == i:  # 현재 검사하는 수는 건너뜁니다.
            end -= 1
            continue
        
        # 현재 검사하는 수를 제외한 나머지 수 중에서 합을 찾습니다.
        if arr[start] + arr[end] == target:
            count += 1
            break
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            end -= 1

print(count)
