def solution(i, j, k):
    
    count=0

    for num in range(i,j+1):
        count+=str(num).count(str(k))

    return count

# str로 하면 count하면 '11' 이면 1이 두개있는걸로 인식함