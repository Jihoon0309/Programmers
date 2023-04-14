def solution(k, m, score):
    score.sort()
    box_sum=0

    while len(score)>=m:
        box=[]
        for _ in range(m):
            pop=score.pop()
            box.append(pop)
        box_sum=box_sum+min(box)*m
    return box_sum
        