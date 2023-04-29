def solution(n):
    
    n_bin_one_count=bin(n)[2:].count('1')
    result=n

    while True:
        result+=1
        result_bin_one_count=bin(result)[2:].count('1')
        if result_bin_one_count==n_bin_one_count:
            return result