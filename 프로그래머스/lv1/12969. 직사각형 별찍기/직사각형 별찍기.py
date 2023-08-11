a, b = map(int, input().strip().split(' '))
arr=[]

for i in range(b):
    row=[]
    for j in range(a):
        row.append('*')
    arr.append(row)  
    
for i in range(b):
    print(''.join(arr[i]))
