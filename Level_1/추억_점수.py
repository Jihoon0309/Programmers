def solution(name, yearning, photo):
    result=[]
    name_yearning_dict={}
    for i in range(len(name)):
        name_yearning_dict[name[i]]=yearning[i]

    for j in range(len(photo)):
        score=0
        for z in range(len(photo[j])):
            if photo[j][z] in name:
                score+=name_yearning_dict[photo[j][z]]
        result.append(score)

    return result