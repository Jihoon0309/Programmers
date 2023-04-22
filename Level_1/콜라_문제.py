def solution(a, b, n):
    count=0

    while n>=a:
        service=(n//a)*b
        count=count+service
        n=n%a+service
    
    return count