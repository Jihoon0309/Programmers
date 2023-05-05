def solution(want, number, discount):
    
    for dis_in in want:
        if dis_in not in discount:
            return 0
    
    want_dict=dict(zip(want,number))
    want_dict=sorted(want_dict.items())
    count=0

    for i in range(len(discount)-9):
        sale={}
        for j in range(10):
            if discount[i+j] not in sale:
                sale[discount[i+j]]=1
            else:
                sale[discount[i+j]]+=1
        sale=sorted(sale.items())
        if want_dict==sale:
            count+=1

    return count

# for 문 하나만으로 풀이가능