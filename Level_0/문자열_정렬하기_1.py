import re
def solution(my_string):
    number=re.findall(r'\d',my_string)
    answer=list(map(int,number))
    answer.sort()
    return answer


# re 사용하여 숫자 찾고 정렬