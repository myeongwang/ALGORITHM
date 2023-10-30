def solution(rsp):
    dict={'0':'5','2':'0','5':'2'}
    answer =''
    for i in rsp:
        answer+=dict[i]
    return answer     

"""
def solution(rsp):
    arr=[]
    for i in rsp:
        if i=='2':
            arr.append(0)
        elif i=='0':
            arr.append(5)
        else:
            arr.append(2)
    return ''.join(map(str,arr))
"""
