import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap)) # heappop(heap,max(heap))은 사용 불가 

    if not heap:
        return [0, 0]

    return [max(heap), min(heap)]