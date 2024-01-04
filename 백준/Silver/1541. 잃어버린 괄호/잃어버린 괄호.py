expression = input().strip()  # 입력 문자열을 읽어옵니다.
parts = expression.split('-')  # '-'를 기준으로 수식을 나눕니다.

total = sum(map(int,parts[0].split('+')))

for part in parts[1:]:
    total-=sum(map(int,part.split('+')))

print(total)