# 날짜를 일 수로 변환하는 함수 정의
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

# 약관 종류와 유효기간을 months 딕셔너리에 저장
# terms 리스트의 각 원소를 분리하여 약관 종류와 유효기간을 추출하고 months에 저장
def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        # 각 개인정보의 수집 일자와 유효기간을 일 수로 변환하여 비교하여 유효한지 확인
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
