def solution(n):
    result=[0,1]
    for i in range(2,n+1):
        result.append(result[i-2]+result[i-1])
    return result[-1]%1234567


print(solution(0))