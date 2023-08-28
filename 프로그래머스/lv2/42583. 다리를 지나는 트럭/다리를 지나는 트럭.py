def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []  # 다리 위에 있는 트럭을 관리하는 리스트
    
    while truck_weights:
        time += 1
        
        if on_bridge and time - on_bridge[0][1] == bridge_length:
            on_bridge.pop(0)  # 다리에서 나가는 트럭 처리
        
        # 다리 위에 있는 트럭들의 무게의 합을 계산합니다.
        total_weight_on_bridge = 0
        for truck in on_bridge:
            total_weight_on_bridge += truck[0]

        # 현재 다리에 올리려는 트럭의 무게를 더해도 다리가 견딜 수 있는 무게를 넘지 않는지 확인합니다.
        if total_weight_on_bridge + truck_weights[0] <= weight:
            # 트럭을 다리 위에 올릴 수 있습니다.
            truck = truck_weights.pop(0)
            on_bridge.append((truck, time))  # 다리에 트럭 추가
    
    # 마지막 트럭이 다리를 건너는 시간까지 더해줌
    return on_bridge[-1][1] + bridge_length

        