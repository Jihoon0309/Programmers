def solution(s):
    
    word=s.split(' ')
    
    for i in range(len(word)):
        if len(word[i])==0:
            continue
        else:
            word[i]=word[i][0].upper()+word[i][1:].lower()

    result=' '.join(word)

    return result
