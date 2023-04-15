def solution(number, limit, power):
    result=[]

    for i in range(1,number+1):
        count=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                count+=1
                if j!=i//j:
                    count+=1
        if count>limit:
            count=power
        result.append(count)
        
    return (sum(result))

#약수 구할때 모든수 돌리면 시간 오래걸림 루트씌워서 돌리는거 생각