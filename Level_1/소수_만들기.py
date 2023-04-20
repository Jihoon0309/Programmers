from itertools import combinations
def solution(nums):
    
    list_num=list(combinations(nums,3))
    count=0
    
    for i in range(len(list_num)):
        check=True
        for j in range(2,sum(list_num[i])):
            if sum(list_num[i])%j==0:
                check=False
                break
        if check is True:
            count+=1
    
    return count

# combinations 해서 풀면 속도가 더 빠름