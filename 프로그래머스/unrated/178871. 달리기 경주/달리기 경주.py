def solution(players, callings):
    
    index_dict={player: i for i,player in enumerate(players)} #enumerate는(index,value) 
                                                              #dict는 {value,index} 라는걸 기억합시다
    for calling in callings:
        i = index_dict[calling]
        players[i], players[i-1] = players[i-1], players[i] # 변수 스왑 직접 지원 
                                                            # 변수 스왑하는 표준적인 방법 ㅅ2ㅂ
                                                            #풀어쓰는거랑 다름
        index_dict[players[i]] =i
        index_dict[players[i-1]] =i-1
        
    return players
