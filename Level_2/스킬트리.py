def solution(skill, skill_trees):
    
    skill_list=list(skill)
    result=len(skill_trees)

    for i in range(len(skill_trees)):
        order=0
        for j in skill_trees[i]:
            if skill_list[order]!=j:
                if j in skill_list:
                    result-=1
                    break
            else:
                order+=1
                if order==len(skill):
                    break

    return result