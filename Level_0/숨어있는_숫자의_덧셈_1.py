import re
def solution(my_string):
    number=re.findall(r'\d',my_string)
    numbers=list(map(int,number))
    answer=sum(numbers)
    return answer


# 문자열에서 숫자만 빼내는거 알고가기
# import re
# re.sub(pattern, repl, string)
# pattern=r'[^0-9]'
# repl=''


# List로 리턴
# re.findall(pattern, string)
# pattern=r'\d+' +는 1회 이상 반복되는 숫자들에 대한 패턴 의미
# r'\d' 는 1개의 숫자 의미