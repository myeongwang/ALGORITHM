s = input().strip() 

s_count = 1  

for i in range(1, len(s)):
    if s[i] != s[i - 1]:  
        s_count += 1  

result = s_count // 2
print(result)



    