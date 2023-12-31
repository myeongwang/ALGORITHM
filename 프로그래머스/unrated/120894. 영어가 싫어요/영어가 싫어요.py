def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        print(f"Index: {num}, Value: {eng}")
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
"""
import re

def solution(numbers):
    s=''
    dic={'zero':'0',
         'one':'1',
         'two':'2',
         'three':'3',
         'four':'4',
         'five':'5',
         'six':'6',
         'seven':'7',
         'eight':'8',
         'nine':'9'
    }
    for i in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)',numbers):
    	s+=dic[i]
    return int(s)
    
    """