def solution(num_list, n):
    answer = []
    
    for _ in range(0,len(num_list),n):
        answer.append(num_list[:n])
        del num_list[:n]
        
    return answer

#del 잘 생각해서 풀기 이렇게 안풀고 그냥 쉽게 푸는 방법도있음

''' answer=[] 
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
'''
