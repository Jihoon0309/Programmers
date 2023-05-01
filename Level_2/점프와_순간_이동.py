def solution(n):
    count=1
    
    while n!=1:
        if n%2!=0:
            n=n-1
            count+=1
        else:
            n=n/2
        
    return count


# else n//2 하면 프로그래머스 오류 뜸 이유 찾기