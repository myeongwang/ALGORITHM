def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0
    interval = n

    for start in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval:
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start]

    return res