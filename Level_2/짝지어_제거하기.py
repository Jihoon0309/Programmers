def solution(s):
    list_s=list(s)
    save_s=[]
    
    while True:
        save_s.append(list_s[0])
        for i in range(1,len(list_s)):
            if save_s and list_s[i]==save_s[-1]:
                save_s.pop()
            else:
                save_s.append(list_s[i])
        if len(save_s)==0:
            return 1
            break
        else:
            return 0
            break

# 반복문 한번으로 가능함 다시 반복문 1번으로 다시 풀어보기

'''
def solution(s):
    list_s=[]
    
    for i in s:
        if i not in list_s:
            list_s.append(i)
        else:
            if list_s[-1]==i:
                list_s.pop()
            else:
                list_s.append(i)
    if list_s:
        return 0
    else:
        return 1
'''
# 다시 푼 코드 전체적으로 한번 더 안돌아가도됨 왜냐하면 바로바로 제거하기 대문에