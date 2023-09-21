def solution(players, callings):
    index_dict = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        i = index_dict[calling]
        players[i], players[i-1] = players[i-1], players[i]
        
        index_dict[players[i]] = i
        index_dict[players[i-1]] = i - 1
        
    return players
