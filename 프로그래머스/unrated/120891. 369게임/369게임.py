import re
def solution(order):
    order= str(order)
    return len(re.findall('[369]',order)) #re.findall 함수는 주어진 패턴과 일치하는 모든 부분 문자열을 리스트로 반환




"""
def solution(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

def solution(order):
    order = list(str(order))
    count=0
    
    for i in order:
        if i == '3' or i == '6' or i == '9':
            count += 1
            
    return count
"""
           