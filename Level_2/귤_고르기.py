def solution(k, tangerine):
    count=1
    count_list=[]
    result=0
    tangerine.sort()

    for i in range(len(tangerine)):
        if i==len(tangerine)-1:
            count_list.append(count)
        elif tangerine[i]==tangerine[i+1]:
            count+=1
        elif tangerine[i]!=tangerine[i+1]:
            count_list.append(count)
            count=1

    count_list.sort(reverse=True)
    for i in count_list:
            if k>0:
                k-=i
                result+=1
            else:
                break
        
    return result