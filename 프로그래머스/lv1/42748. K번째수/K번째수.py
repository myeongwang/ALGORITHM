def solution(array, commands):
    arr=[]
    
    for command in commands:
        i, j, k = command  # command에서 i, j, k 값을 추출
        
        sub_array = array[i-1:j]  # i부터 j까지의 부분 배열을 추출
        sub_array.sort()  # 부분 배열을 정렬
        kth_number = sub_array[k-1]  # 정렬된 부분 배열에서 k번째 수 추출
        
        arr.append(kth_number)  # 추출한 k번째 수를 정답 배열에 추가
    return arr    