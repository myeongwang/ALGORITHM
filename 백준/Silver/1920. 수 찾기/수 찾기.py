def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(array, target, 0, N - 1))
