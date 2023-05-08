def solution(today, terms, privacies):
    def all_day(date):
        year,month,day=map(int,date.split('.'))
        return (year*12*28)+(month*28)+day

    todays=all_day(today)
    pri_days=[]
    result=[]

    for i in range(len(privacies)):
        pri_days.append(all_day(privacies[i][0:10]))
        for j in range(len(terms)):
            if terms[j][0] in privacies[i]:
                pri_days[i]+=int(terms[j][2:])*28

    for j in range(len(pri_days)):
        if pri_days[j]<=todays:
            result.append(j+1)
    return result

# 모든 날짜를 day로 만드는 함수 만들기 이때 map함수 사용하면 쉽게 만들수있음