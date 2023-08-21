"""
def solution(people,limit):
    people.sort()
    answer=0

    for i in range(1,len(people)):
        
        if people[i-1]+people[i]==limit:
            if i==1:
                answer= len(people)-1   
                return answer
            answer= int(i/2)+(len(people)-i)
            return answer
        elif people[i-1]+people[i]>limit:
            if i==1:
                answer= len(people)
                return answer
            answer=int(i/2)+(len(people)-i+1)
            return answer"""
def solution(people, limit):
    people.sort()  # 사람들을 무게 순으로 정렬
    answer = 0
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    
    return answer