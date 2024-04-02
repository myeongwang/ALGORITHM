import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 첫 번째 리스트 n1의 길이와 요소들 입력받기
n = int(input())
n1 = set(map(int, input().split()))

# 두 번째 리스트 m1의 길이와 요소들 입력받기
m = int(input())
m1 = list(map(int, input().split()))

# 두 번째 리스트 m1의 각 요소에 대해 반복하여 첫 번째 리스트 n1에 포함되어 있는지 확인
for num in m1:
    if num in n1:
        print(1)  # 찾는 값이 있으면 1 출력
    else:
        print(0)  # 찾는 값이 없으면 0 출력
