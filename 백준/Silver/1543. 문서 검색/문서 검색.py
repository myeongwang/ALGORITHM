import sys
input = sys.stdin.readline

# strip() 으로 \n 는 삭제
doc = input().strip()
word = input().strip()
count, start = 0, 0

while start <= len(doc) - len(word):
    if doc[start:start + len(word)] == word:
        count += 1
        start += len(word)
    else:
        start += 1

print (count)