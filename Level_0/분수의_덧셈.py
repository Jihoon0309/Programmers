numer1, denom1, numer2, denom2 = 1, 2, 3, 4

numer=(denom1*numer2)+(denom2*numer1)
denom=denom1*denom2


for i in range(max(numer, denom),0,-1):
    if numer%i==0 and denom%i==0:
        break

result=[numer//i,denom//i]
print(result)

# 최대공약수 찾아서 나눠주기