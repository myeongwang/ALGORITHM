
def solution(s):
    answer = ""
    capitalize_next = True  # 다음 글자를 대문자로 변환해야 하는지 여부

    for char in s:
        if char == " ":  # 공백 문자일 경우
            answer += char  # 그대로 추가
            capitalize_next = True  # 다음 글자를 대문자로 변환해야 함
        elif capitalize_next:  # 대문자로 변환해야 하는 글자일 경우
            answer += char.upper()  # 대문자로 변환하여 추가
            capitalize_next = False  # 다음 글자는 소문자로 유지
        else:
            answer += char.lower()  # 소문자로 변환하여 추가
            capitalize_next = False  # 다음 글자는 소문자로 유지

    return answer
    
    
                
    
    
    







    