n, m = map(int, input().split())  # 두 개의 정수 n과 m을 입력받음

for _ in range(m):  # 세로의 길이 m만큼 반복
    print('*' * n)  # 가로의 길이 n만큼 별(*) 문자 출력
