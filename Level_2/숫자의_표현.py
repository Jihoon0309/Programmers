def solution(n):
    num=1
    cnt=1
    
    while num!=n:
        num_2=num
        sum=num
        while sum<n:
            num_2+=1
            sum+=num_2
        if sum==n:
            cnt+=1
        num+=1
            
    return cnt

# for 문으로 더 간결하게 보기좋게 할 수 있을듯