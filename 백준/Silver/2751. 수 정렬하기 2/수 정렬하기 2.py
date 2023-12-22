import sys

n = int(sys.stdin.readline().strip())
numbers = []

for _ in range(n):
    number = int(sys.stdin.readline().strip())
    numbers.append(number)

numbers.sort()

# 결과 출력
sys.stdout.write('\n'.join(map(str, numbers)))

    