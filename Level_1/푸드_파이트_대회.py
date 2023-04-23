def solution(food):
    tmp=[]
    result=[]

    for i in range(1,len(food)):
        if food[i]>=2:
            for j in range(food[i]//2):
                result.append(str(i))
                tmp.append(str(i))
    result.append(str(0))
    while len(tmp)!=0:
        pop=tmp.pop()
        result.append(pop)

    answer=''.join(result)
    return answer