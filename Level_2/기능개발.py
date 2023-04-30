def solution(progresses, speeds):
    completion_list=[]
    
    for i in range(len(progresses)):
        sum=progresses[i]
        completion=0
        while sum<100:
            sum+=speeds[i]
            completion+=1
        completion_list.append(completion)

    result=[]
    days=1
    max=completion_list[0]
    
    for i in range(1,len(completion_list)):
        if max<completion_list[i]:
            max=completion_list[i]
            result.append(days)
            days=1
        else:
            days+=1
    result.append(days)

    return result
