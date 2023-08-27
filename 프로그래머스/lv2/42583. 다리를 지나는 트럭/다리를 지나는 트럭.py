def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []  # 다리 위에 있는 트럭을 관리하는 리스트
    
    while truck_weights:
        time += 1
        
        if on_bridge and time - on_bridge[0][1] == bridge_length:
            on_bridge.pop(0)  # 다리에서 나가는 트럭 처리
        
        if sum([truck[0] for truck in on_bridge]) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            on_bridge.append((truck, time))  # 다리에 트럭 추가
    
    # 마지막 트럭이 다리를 건너는 시간까지 더해줌
    return on_bridge[-1][1] + bridge_length

        