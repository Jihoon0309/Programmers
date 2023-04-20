def solution(str1, str2):

    # 알페벳을 대문자로 바꿔줌
    str1, str2 =str1.upper(), str2.upper()
    
    # 알파벳만 2개씩 나눠서 저장
    def clustering(str):
        clustering_list=[]
        for i in range(len(str)-1):
            if str[i:i+2].isalpha():
                clustering_list.append(str[i:i+2])
        return clustering_list

    str1, str2= clustering(str1), clustering(str2)

    # 둘중 하나라도 값이 없는경우 65536으로 바로 끝내기
    if not (str1 or str2):
        return 65536
    
    # 다중집합 합집합
    str1_temp=str1.copy()
    union=str1.copy()
    for i in str2:
        if i not in str1_temp:
            union.append(i)
        else:
            str1_temp.remove(i)

    # 다중집합 교집합
    intersection=[]
    for j in str2:
        if j in str1:
            intersection.append(j)
            str1.remove(j)

    # 65536곱한후 정수부만 출력
    result=int((len(intersection)/len(union))*65536)
    return result

# 이때 isalpha()함수 기억하기 그리고 다중집합(합집합, 교집합) 새로 배웠음 