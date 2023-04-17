def solution(s):
    result=0

    while len(s)!=0:
        word_1=0
        word_2=0
        word=s[0]
        while True:
            if s[0]==word:
                word_1+=1
            else:
                word_2+=1
            s=s[1:]
            if word_1==word_2 or len(s)==0:
                result+=1
                break
    return result

# 맨마지막에 s의 길이가 0일때 생각하기