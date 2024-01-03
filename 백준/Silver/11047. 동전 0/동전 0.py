import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

def min_coin_count(N, M, coin_values):
    coin_values.sort(reverse=True)  # 동전 가치를 내림차순으로 정렬

    count = 0  # 동전 개수를 저장할 변수

    for coin in coin_values:
        if M >= coin:
            num_coins = M // coin
            count += num_coins
            M -= num_coins * coin

    if M != 0:
        return -1  # 남은 잔돈을 모두 동전으로 바꿀 수 없는 경우

    return count

# 함수 실행
result = min_coin_count(N, M, coin_values)
print(result)
