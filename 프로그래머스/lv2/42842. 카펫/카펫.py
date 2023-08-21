import math

def solution(brown, yellow):
    total_size = brown + yellow
    
    for h in range(1, int(math.sqrt(total_size)) + 1):
        if total_size % h == 0:
            w = total_size // h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]