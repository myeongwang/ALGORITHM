
2
3
4
5
6
7
8
9
10
11
12
13
def solution(n, words):
    arr = []

    for i in range(1, len(words)):  # 1부터 시작하여 인덱스 i를 사용하여 words 리스트를 반복
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            # words[i]가 words 리스트의 앞에서부터 i까지에 이미 등장하거나,
            # 또는 words[i-1]의 끝말과 words[i]의 첫말이 다를 경우
            arr = [(i % n) + 1, (i // n) + 1]  # i를 행과 열 정보로 변환하여 저장
            return arr  # 결과 반환

    arr = [0, 0]  # 모든 단어가 규칙을 따르는 경우의 결과
    return arr