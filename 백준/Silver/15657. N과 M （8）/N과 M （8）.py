def combinations(arr, selected, index, start, m):
    if index == m:
        print(" ".join(map(str, selected)))
        return

    for i in range(start, len(arr)):
        selected[index] = arr[i]
        combinations(arr, selected, index + 1, i, m)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()  # 입력된 숫자를 정렬합니다.

selected = [0] * M  # 선택된 숫자를 저장할 배열

combinations(numbers, selected, 0, 0, M)