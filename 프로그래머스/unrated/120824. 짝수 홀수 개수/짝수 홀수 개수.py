def solution(num_list):
    n=0
    result=[0,0]
    while True:
        if num_list[n] %2==0:
            result[0]+=1
        else:
            result[1]+=1
        n+=1
        if n== len(num_list):
            break
    return result    