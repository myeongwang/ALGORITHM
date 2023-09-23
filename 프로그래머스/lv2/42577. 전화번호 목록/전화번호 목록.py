def solution(phone_book):
    phone_dict = {}  # 해시맵으로 전화번호를 저장할 딕셔너리를 생성합니다.
    
    # 전화번호를 해시맵에 저장합니다.
    for phone_number in phone_book:
        phone_dict[phone_number] = True
        
    
    # 다른 전화번호를 순회하면서 각 전화번호의 접두어가 해시맵에 있는지 확인합니다.
    for phone_number in phone_book:
        current_number = ""
        for digit in phone_number:
            current_number += digit
            if current_number != phone_number and current_number in phone_dict:
                return False
    
    return True

    