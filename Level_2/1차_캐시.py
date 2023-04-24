def solution(cacheSize, cities):
    city_list=[]
    result=0
    cities_lower=[i.lower() for i in cities] # 소문자로 만들기


    if cacheSize==0:
        result=len(cities)*5
    else:
        for city in cities_lower:
            if city not in city_list:
                city_list.append(city)
                result+=5
                if len(city_list)>cacheSize:
                    city_list.pop(0)
            else:
                city_list.remove(city)
                city_list.append(city)
                result+=1
    return result
