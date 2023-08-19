"""
def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
"""
def solution(s):
    stack=[]

    for char in s:
        if char =="(":
            stack.append(char)
        elif char ==")":
            if not stack: #스택이 비었다면
                return False
            stack.pop()
    return len(stack)==0        
            
        
