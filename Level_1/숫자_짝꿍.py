def solution(X, Y):
    answer = ''
    
    for i in range(9,-1,-1) :
        minimum=min(X.count(str(i)), Y.count(str(i))) # 만약 X와 Y에 모두 0이 아니면 그중 작게 있는 값을 저장
        answer+=str(i)*minimum

    if answer == '' :
        return '-1'
    elif answer[0]=='0':
        return '0'
    else :
        return answer
# X를 Y에 하나하나 비교해서 시간초과나서 딕셔너리로 만들었는데 그냥 카운트 함수쓰면 더 빠름
# 너무 어렵게만 생각하지 말기
'''
첫번째 풀이 
def solution(X, Y):
    list_Y=list(Y)
    list_X=list(X)
    dict_X={i:0 for i in range(10)}
    dict_Y={i:0 for i in range(10)}
    result=[]

    for i in list_X:
        dict_X[int(i)]+=1

    for i in list_Y:
        dict_Y[int(i)]+=1

    for j in reversed(dict_Y):
        if dict_X[j]==0 or dict_Y[j]==0:
            continue
        if dict_X[j]>dict_Y[j]:
            result.append(str(j)*(dict_Y[j]))
        else:
            result.append(str(j)*(dict_X[j]))

    if not result:
        return '-1'
    elif int(result[0])==0:
        return '0'
    else:
        answer=''.join(result)
        return answer
'''