"""
def solution(n):
    fib_0=0
    fib_1=1
    for i in range(0,n):
      fib_0=fib_1 
      fib_1+=fib_0
    return fib_0 
    """

def solution(n): #이게 파이썬 코드지
    a,b=0,1
    for i in range(0,n):
        a,b=b,(a+b) %1234567 #is closer to temp=a a=b b=temp+a 위에 풀이랑 당연히 다름 
    return a


"""
def solution(n):
    a,b=0,1
    for i in range(0,n):
        temp=a  #temp 쓰는 이유는 기본적으로 컴퓨터는 값을 덮어쓰기 때문에 temp에 미리 뺴놨다가 쓰는거 
        a=b
        b=temp+a
    return a        
"""