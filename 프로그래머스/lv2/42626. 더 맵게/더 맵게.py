import heapq

def solution(scoville, K):
    # scoville 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    
    mix_count = 0
    
    while scoville:
        # 가장 작은 스코빌 지수의 음식을 꺼내기
        min1 = heapq.heappop(scoville)
        
        if min1 >= K:
            return mix_count
        
        if not scoville:
            return -1
        
        # 두 번째로 작은 스코빌 지수의 음식을 꺼내기
        min2 = heapq.heappop(scoville)
        
        # 두 음식을 섞어서 새로운 음식의 스코빌 지수 계산
        new_scoville = min1 + (min2 * 2)
        
        # 새로운 음식의 스코빌 지수를 다시 힙에 추가
        heapq.heappush(scoville, new_scoville)
        
        mix_count += 1
    
    return -1





