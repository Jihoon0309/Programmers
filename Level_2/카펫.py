def solution(brown, yellow):
    sum=brown+yellow
    result=[]
    
    for i in range(1,int(sum**0.5)+1):
        if sum%i==0:
            result.append(i)
            
    for j in range(len(result)-1,0,-1):
        if yellow%((sum/result[j])-2)==0:
            hor=result[j]
            break        
            
    return [sum//hor,hor]

# 만약 약수의 개수/2 가 짝수일때를 생각해야함 이때는 숫자가 다름
