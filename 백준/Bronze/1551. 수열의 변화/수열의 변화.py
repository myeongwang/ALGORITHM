# 입력 받기
n, k = map(int, input().split())
sequence = list(map(int, input().split(',')))

# 주어진 연산을 수행하는 함수 정의
def transform(seq):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i+1] - seq[i])
    return new_seq

# k번의 연산을 수행하여 변형된 수열 구하기
for _ in range(k):
    sequence = transform(sequence)

# 결과 출력
print(','.join(map(str, sequence)))
