def solution(n):
    result_list=[0,1]
    for i in range(1,n+1):
        result_list.append(result_list[i]+result_list[i-1])
    return result_list[-1]%1234567

# 피보나치 수열 사용