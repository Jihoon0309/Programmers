def solution(array, n):
    num=100
    array.sort()
    for i in array:
        if num>abs(n-i):
            num=abs(n-i)
            result=i
    
    return result

# array를 sort 사용하여 순서대로 맞춰야함 가까운 수가 2개일때 작은 수를 return 하기 위함