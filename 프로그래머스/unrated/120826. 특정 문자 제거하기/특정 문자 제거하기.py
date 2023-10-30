"""
def solution(my_string, letter):
    a= list(my_string)
    for i in range(len(a)-1,-1,-1):
        if a[i]==letter:
            a.pop(i)
    return ''.join(a)
    """
def solution(my_string, letter):
    return my_string.replace(letter,"")
    