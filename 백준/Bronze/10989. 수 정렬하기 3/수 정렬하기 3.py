import sys

n = int(sys.stdin.readline().strip())  # 입력 받는 방법을 최적화

# 입력된 수의 개수를 카운트하는 배열 생성
count = [0] * 10001

# 수를 입력 받아 카운트 배열에 개수를 기록
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

# 카운트 배열을 기반으로 정렬된 결과 출력
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
