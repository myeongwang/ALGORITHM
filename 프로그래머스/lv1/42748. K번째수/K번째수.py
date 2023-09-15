def solution(array, commands):
    answer = []  # 결과를 저장할 리스트
    
    
    for command in commands:
        i,j,k=command
        sub_array=array[i-1:j]
        sorted_sub_array=sorted(sub_array) #sort() 메서드는 원본 리스트를 정렬하고 반환 값은 None입
        answer.append(sorted_sub_array[k-1])
    
    return answer

