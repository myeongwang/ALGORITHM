import sys
input = sys.stdin.readline

def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        # 양끝이 동일하면 하나씩 앞으로 당김
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            pseudo_left = word[left + 1:right + 1]
            pseudo_right = word[left:right]
            if pseudo_left == pseudo_left[::-1] or pseudo_right == pseudo_right[::-1]:
                return 1
            else:
                return 2
    return 0

T = int(input()) #테스트케이스

for i in range(T):
    N = input().strip()
    print(is_palindrome(N))