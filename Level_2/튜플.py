def solution(s):
    s=s[2:-2]
    s=(s.split('},{'))
    s.sort(key=len) # 문자열 길이 기준으로 정렬
    result=[]
    
    for i in s:
        num=i.split(',')
        int_num=list(map(int,num))
        for j in int_num:
            if j not in result:
                result.append(j)
            
    return result
    

# 양쪽의 "{{ , }}" 없애고 },{ 자르고 문자열을 문자열 길이 기준으로 정렬