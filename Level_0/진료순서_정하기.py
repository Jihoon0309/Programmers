def solution(emergency):

    order=sorted(emergency, reverse=True)
    result=[]
    for i in emergency:
        result.append(order.index(i)+1)
    return result

#딕셔너리 사용하면 속도가 더 빨라짐 index함수 시간복잡도가 O(n)이기때문에 반복문안에 들어가면 O(n^2) 이기때문

# emergency=[3,76,24,43,11,2,5,113,3530,39433,13,39,6,357,34534,78768678,343343,1332,756,7680,324324]
# order=sorted(emergency, reverse=True)
# order_dict={}
# result=[]
# for i in range(len(order)):
#     order_dict[order[i]]=i+1

# for j in emergency:
#     result.append(order_dict[j])
# print(result)

#이런식으로 고치는게 좋을듯
