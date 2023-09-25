def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i==0 or arr[i]!= arr[i-1]: #중복제거할 때는 remove쓰면 안됨.
            answer.append(arr[i])
      
    return answer