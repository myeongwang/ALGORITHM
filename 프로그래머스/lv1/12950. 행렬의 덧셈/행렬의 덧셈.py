import numpy as np

def solution(A,B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    
    return result.tolist()