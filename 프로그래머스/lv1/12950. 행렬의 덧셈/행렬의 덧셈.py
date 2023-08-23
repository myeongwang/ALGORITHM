def solution(arr1, arr2):
    arr3=[]
    
    for i in range(len(arr1)):
        row=[]
        for j in range(len(arr1[0])):
            row.append(arr1[i][j]+arr2[i][j])
        arr3.append(row)    
    return arr3    

"""
import numpy as np

def sumMatrix(A,B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    return result.tolist()
    """
