t = int(input())  # 테스트 케이스 수 입력

for _ in range(t):
    n = int(input())  # 배열의 크기 입력
    arr = list(map(int, input().split()))  # 배열의 요소 입력

    min_val = min(arr)  # 배열에서 최소값 구하기
    max_val = max(arr)  # 배열에서 최대값 구하기

    print(min_val, max_val)
