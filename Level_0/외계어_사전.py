def solution(spell, dic):
    answer=2
    
    for i in dic:
        count=0
        for j in spell:
            if j not in i:
                break
            else:
                count+=1
        if count==len(spell):
            answer=1
            break

    return answer


#너무 어렵게 생각함 정렬해서 푸는방법이 훨씬 좋을듯