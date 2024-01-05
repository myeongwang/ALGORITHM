from itertools import combinations

def counts(arr):
    for i in combinations(arr, 7):
        if sum(i) == 100:
            return sorted(i)

arr = []

for _ in range(9):
    arr.append(int(input()))

result = counts(arr)

for height in result:
    print(height)
