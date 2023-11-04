def solution(array, n):
    array.append(n)
    array.sort()
    i = array.index(n)
    
    if i == 0:
        return array[i+1]
    elif i == len(array) - 1:
        return array[i-1]
    else:
        # 두 후보 중에서 n과의 차이가 더 작은 숫자를 반환
        return min((array[i-1], array[i+1]), key=lambda x: abs(x-n))

    
    
    