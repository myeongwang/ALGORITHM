n= list(map(int,input().strip()))

n.sort(reverse = True)

number = ''.join(map(str,n))
print(number)
