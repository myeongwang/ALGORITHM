import sys

input = sys.stdin.readline

h,m = map(int,input().split())

if m-45>=0:
    print(h , m-45)
elif (m-45<0) and h-1>=0 :
    print(h-1 , m+15)
else:
    print(23 , m+15)
    