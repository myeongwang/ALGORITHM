def is_valid(s):
    stack = []  # 스택 초기화

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]  # 문자열 회전 
        if is_valid(rotated):  # 올바른 괄호 문자열인지 판단
            answer += 1
    
    return answer