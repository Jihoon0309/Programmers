def solution(t, p):
    word=''
    count=0

    for i in range(len(t)-len(p)+1):
        word=(t[i:i+len(p)])
        if int(word)<=int(p):
            count+=1
    return count