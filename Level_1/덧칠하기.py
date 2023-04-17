def solution(n, m, section):
    count=0
    
    while section:
        del_num=m+section[0]
        if del_num>section[-1]:
            count+=1
            break
        else:    
            while section and section[0]<del_num:
                section.pop(0)
        count+=1
        
    return count

# 반복문 한번만으로 풀수있음