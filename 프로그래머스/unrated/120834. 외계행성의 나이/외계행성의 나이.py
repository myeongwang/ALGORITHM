def solution(age):
    answer = 'abcdefghij'
    return ''.join(map(lambda x: answer[int(x)],str(age)))