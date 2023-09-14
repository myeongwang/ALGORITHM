import numpy as np

def solution(A,B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    
    numpy_array = np.array([1, 2, 3, 4, 5])
    result_1 = numpy_array.tolist()

    print(result_1)
    return result.tolist()