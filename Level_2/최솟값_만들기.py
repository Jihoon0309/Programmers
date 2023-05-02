def solution(A,B):
    result=0
    A.sort()
    B.sort()
    for i in range(len(A)):
        result+=A[i]*B[-i-1]
    return result