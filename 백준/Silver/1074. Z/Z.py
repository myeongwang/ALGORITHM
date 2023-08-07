"""
def recursion(N,r,c): # 재귀 이용 시 런타임 에러 발생
    if size == 1:
        return 0
    half = size // 2
    if row < half and col < half:
        return Z(row, col, half)
    if row < half and col >= half:
        return half * half + Z(row, col - half, half)
    if row >= half and col < half:
        return 2 * half * half + Z(row - half, col, half)
    return 3 * half * half + Z(row - half, col - half, half)

N, r, c = map(int, input().split())
print(recursion(r, c, 2 ** N))
"""

N, r, c = map(int, input().split())
size = 2 ** N
result = 0

while size > 1:
    half = size // 2

    if r < half and c < half:
        size = half
    elif r < half and c >= half:
        size = half
        result += half * half
        c -= half
    elif r >= half and c < half:
        size = half
        result += 2 * half * half
        r -= half
    else:
        size = half
        result += 3 * half * half
        r -= half
        c -= half

print(result + r * size + c)