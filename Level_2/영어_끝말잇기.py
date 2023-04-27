def solution(n, words):
    num=1
    add_words=[words[0]]
    
    for i in range(1,len(words)):
        num+=1
        if (words[i] in add_words) or (add_words[-1][-1]!=words[i][0]):
            if num%n==0:
                return [n,num//n]
            else:
                return [num%n,num//n+1]
            break
        else:
            add_words.append(words[i])

    return [0,0]