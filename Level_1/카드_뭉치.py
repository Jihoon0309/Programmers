def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and cards1[0]==i:
            del cards1[0]
        elif cards2 and cards2[0]==i:
            del cards2[0]
        else:
            return 'No'
    return 'Yes'

#goal을 없애려고 안해도됨 너무 어렵게 생각 하지않기