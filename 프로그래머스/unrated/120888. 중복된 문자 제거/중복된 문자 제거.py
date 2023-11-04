def solution(my_string):
    print(dict.fromkeys(my_string))
    return ''.join(dict.fromkeys(my_string))



#key가 아닌 value 반환 원할 시
#my_dict = dict.fromkeys(my_string, 'value')

"""
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
"""