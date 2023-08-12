#boj 10808 array 복습

def count_alphabet(s):
  alphabet_count=[0]*26

  for c in s:
    if 'a'<=c<='z':
      index = ord(c)-ord('a')
      alphabet_count[index]+=1

  return alphabet_count    
  

input_string = input().strip().lower()
result = count_alphabet(input_string)

print(' '.join(map(str,result)))