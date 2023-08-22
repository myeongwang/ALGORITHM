def gcd(a, b):
    # 최대공약수를 구하는 함수
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 최소공배수를 구하는 함수
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]  # 최종 결과값 초기화, 초기값은 주어진 리스트의 첫 번째 원소
    for num in arr[1:]:
        # 주어진 리스트의 나머지 원소들과 최소공배수를 구해 갱신
        answer = lcm(answer, num)
    return answer