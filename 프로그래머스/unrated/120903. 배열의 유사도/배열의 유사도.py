def solution(s1,s2):
    return len(set(s1) & set(s2))


"""
def solution(s1, s2):
    count = 0
    for string in s1:
        count += s2.count(string)
    return count
"""


