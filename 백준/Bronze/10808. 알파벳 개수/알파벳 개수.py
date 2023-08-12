def count_alphabet(s):
    alphabet_count = [0] * 26  # 알파벳 개수를 저장할 리스트 초기화

    for c in s:
        if 'a' <= c <= 'z':
            index = ord(c) - ord('a')  # 알파벳이면 인덱스 계산
            alphabet_count[index] += 1  # 해당 알파벳 개수 증가

    return alphabet_count

def main():
    input_string = input().strip().lower()  # 문자열 입력 (소문자로 변환)
    result = count_alphabet(input_string)

    for count in result:
        print(count, end=' ')

if __name__ == "__main__":
    main()