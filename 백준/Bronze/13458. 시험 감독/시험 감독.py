import math

# 입력 받기
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 필요한 감독관 수 초기화
supervisors = [1] * N

# 각 시험장의 응시자 수에서 총감독관이 감시할 수 있는 응시자 수를 뺍니다.
for i in range(N):
    A[i] -= B

# 남은 응시자 수가 양수면 부감독관이 필요하므로 부감독관 수를 추가합니다.
for i in range(N):
    if A[i] > 0:
        supervisors[i] += math.ceil(A[i] / C)

# 총 감독관 수를 계산합니다.
total_supervisors = sum(supervisors)

# 결과 출력
print(total_supervisors)
