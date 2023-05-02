def solution(s):
    num=list(map(int, s.split(' ')))
    result=str(min(num))+' '+str(max(num))
    return result