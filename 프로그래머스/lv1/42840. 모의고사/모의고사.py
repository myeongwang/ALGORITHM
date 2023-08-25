def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]  # 각 수포자의 점수를 저장하는 리스트

    # 정답 배열과 각 수포자의 패턴을 비교하여 점수 계산
    for i, ans in enumerate(answers):
        if ans == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if ans == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if ans == pattern3[i % len(pattern3)]:
            scores[2] += 1

    max_score = max(scores)  # 가장 높은 점수
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]  # 가장 많이 맞힌 수포자 찾기
    """
    result = []
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
    """

    return result