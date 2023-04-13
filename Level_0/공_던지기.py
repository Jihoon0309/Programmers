def solution(numbers, k):
    arr=[]
    
    if len(numbers)%2==0:
        for i in range(0,len(numbers),2):
            arr.append(numbers[i])
            
    else:
        for i in range(0,len(numbers),2):
            arr.append(numbers[i])
        for j in range(1,len(numbers),2):
            arr.append(numbers[j])
            
    while k>len(arr)-1:
            k-=len(arr)
            
    return arr[k-1]

#홀짝 안나누고 풀수있음 그냥 %로 나머지 구하는 방식으로하면 더 쉽게 풀림 어렵게 생각하지말고 쉽게 생각하기