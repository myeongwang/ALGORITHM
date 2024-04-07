import sys
input= sys.stdin.readline

n,m= map(int,input().split())
arr=[[0]*(n+1)] # 리스트 들어갈 자리 # 여기에는 append 예정
D=[[0]*(n+1) for _ in range(n+1)]# 합 배열 들어갈 자리 #여기에는 초기화 예정

for i in range(n):
    arr_row = [0]+[int(x) for x in input().split()]
    arr.append(arr_row)
    
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j]=D[i-1][j]+D[i][j-1]-D[i-1][j-1] +arr[i][j] 
        # 합 배열 구하기 공식 memory
        
# 합 출력 공식 memory
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2]- D[x1-1][y2]- D[x2][y1-1]+ D[x1-1][y1-1] #1,4/ 3,1
    print(result)
        