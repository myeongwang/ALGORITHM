n = int(input())
stack = []
result = []
count = 1
possible = True

for _ in range(n):
    number = int(input())

    while count <= number:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == number:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print('NO')

    
    