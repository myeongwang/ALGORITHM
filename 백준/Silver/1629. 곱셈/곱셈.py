def recursion(x,n,mod):
  if n==0:
    return 1
  elif n%2 ==0:
    half = recursion(x,n//2,mod)
    return half*half%mod
  else:
    return (x*recursion(x,n-1,mod))%mod    

a,b,c= map(int,input().split())
result = recursion(a,b,c)
print(result)
