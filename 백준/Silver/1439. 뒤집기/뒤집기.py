word = list(map(int,input().strip()))
count = 1

for i in range(1,len(word)):
    if word[i-1]!= word[i]:
        count+=1
print(count//2)        
    
    