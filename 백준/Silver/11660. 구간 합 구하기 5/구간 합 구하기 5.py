import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
A= [[0]*(n+1)] # 행렬 요소 저장공간
D= [[0]*(n+1) for _ in range(n+1)] # 구간 합 행렬 저장공간 존나하고 

for i in range(n): # 행렬 저장
    A_row = [0]+[int(x) for x in input().split()]
    A.append(A_row)
    
for i in range(1,n+1): # 구간합 저장
    for j in range(1,n+1):
        # 합 배열 구현
        D[i][j]= D[i][j-1]+ D[i-1][j]-D[i-1][j-1]+ A[i][j]
        
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2]- D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
    
    