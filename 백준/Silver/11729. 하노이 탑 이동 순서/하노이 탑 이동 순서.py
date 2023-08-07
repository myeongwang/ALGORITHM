#boj 11729 하노이탑

def hanoi(n,start,end,auxiliary):
  if n==1:
    print(start,end)
  else:
    hanoi(n-1,start,auxiliary,end)
    print(start,end)
    hanoi(n-1,auxiliary,end,start)  

  

n=int(input())
print(2**n-1)
hanoi(n,1,3,2)