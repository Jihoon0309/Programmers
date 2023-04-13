def solution(my_string):
    answer=[]
    for i in list(my_string):
        if i not in answer:
            answer.append(i)
    
    return ''.join(answer)

# 중복제거를 하기위해 새로운 배열에 하나씩 넣고 이미 들어가있으면 넣지않음