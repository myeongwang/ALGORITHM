def solution(s):
    s_list=s.split()
    s_list=list(map(int,s_list))
    s_list.sort()
    
    return (str(s_list[0])+" "+str(s_list[len(s_list)-1]))