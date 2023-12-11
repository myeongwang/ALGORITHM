n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))
    
for num in sorted(num_list):
    print(num)
