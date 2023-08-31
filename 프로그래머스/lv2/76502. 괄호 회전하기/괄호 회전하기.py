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
    
    return len(stack) == 0 # 스택이 비어있을 때만 True를 반환하게 되므로, 괄호 문자열이 올바른지 여부를 판단

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:]+s[:i]
        if is_valid(rotated):  # 올바른 괄호 문자열인지 판단
            answer += 1
    
    return answer