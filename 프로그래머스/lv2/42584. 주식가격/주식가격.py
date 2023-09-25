def solution(prices):
    answer = [0] * len(prices)  # 결과를 저장할 리스트 초기화
    stack = []  # 주식 가격의 인덱스를 저장할 스택

    for i in range(len(prices)):
        # 스택이 비어있지 않고 현재 가격이 이전 가격보다 작을 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j  # 현재 시점 - 떨어진 시점 = 가격이 떨어지지 않은 기간
        stack.append(i)  # 현재 인덱스를 스택에 추가

    # 남아 있는 주식 가격들은 끝까지 가격이 떨어지지 않았으므로 처리
    for i in stack:
        answer[i] = len(prices) - i - 1

    return answer