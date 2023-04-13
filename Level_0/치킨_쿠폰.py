def solution(chicken):
    
    result=0
    coupon=0
    
    while chicken!=0:
        coupon=coupon+chicken%10
        chicken=chicken//10
        if coupon>=10:
            coupon-=9
            result+=1
        result=result+chicken
        
    return result

# 치킨숫자를 쿠폰 숫자로 생각하고 다시 풀기