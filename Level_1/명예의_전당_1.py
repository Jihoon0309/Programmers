def solution(k, score):
    box=[]
    result=[]

    for i in score:
        if len(box)==k and i>min(box):
            box.append(i)
            box.remove(min(box))

        elif len(box)<k:
            box.append(i)
        result.append(min(box))
        
    return result