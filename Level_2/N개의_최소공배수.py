def solution(arr):
    mul=1
    
    for i in arr:
        mul*=i

    for i in range(max(arr),mul+1):
        cnt=0
        for j in arr:
            if i%j!=0:
                cnt+=1
                break
            else:
                pass
        if cnt==0:
            break
        
    return i

# 꼭 2중 for문이 없어도 될꺼같음 for문 한개로 다시 풀어보기