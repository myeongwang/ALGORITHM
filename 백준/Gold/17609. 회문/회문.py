import sys
input = sys.stdin.readline

def is_palindrome(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

def solve(word):
    if is_palindrome(word):
        return 0
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            removed_left = word[:left] + word[left+1:]
            removed_right = word[:right] + word[right+1:]
            if is_palindrome(removed_left) or is_palindrome(removed_right):
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 2

T = int(input())  # 테스트케이스 수 입력

for i in range(T):
    N = input().strip()
    result = solve(N)
    print(result)
