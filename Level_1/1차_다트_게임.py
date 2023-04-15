def solution(dartResult):
    
    num=''
    num_list=[]

    for i in dartResult:
        if i.isnumeric():
            num+=i
        elif i=='S':
            num_list.append(int(num))
            num=''
        elif i=='D':
            num_list.append(int(num))
            num_list[-1]**=2
            num=''
        elif i=='T':
            num_list.append(int(num))
            num_list[-1]**=3
            num=''
        elif i=='*':
            if len(num_list)==1:
                num_list[-1]*=2
                num=''
            else:
                num_list[-1]*=2
                num_list[-2]*=2
        elif i=='#':
            num_list[-1]*=(-1)
            
    return sum(num_list)

# 숫자 저장할때 10때문에 바로 리스트에 넣지않았음 