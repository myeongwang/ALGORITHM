def hanoi(n, start, end, auxiliary):
    if n == 1:
        return [[start, end]]
    moves = []
    moves.extend(hanoi(n - 1, start, auxiliary, end))
    moves.append([start, end])
    moves.extend(hanoi(n - 1, auxiliary, end, start))
    return moves
  

def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer