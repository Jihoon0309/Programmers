import numpy as np

def solution(arr1, arr2):
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    result=arr1@arr2
    return result.tolist()

#.tolist() 사용하여 array를 list로 변경시켜줘야함