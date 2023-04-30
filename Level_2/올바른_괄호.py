def solution(s):

    result=[]
    for i in s:
        if not result and i==')':
            return False
        elif i==')':
            result.pop()
        else:
            result.append(i)

    if result:
        return False
    else:
        return True