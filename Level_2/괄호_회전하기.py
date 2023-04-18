def solution(s):
    list_s=list(s)
    count=0

    for _ in range(len(list_s)):
        now=[]
        for i in list_s:
            if i=='(' or i=='[' or i=='{':
                now.append(i)

            elif i==')':
                if now and now[-1]=='(':
                    del now[-1]
                else:
                    now.append(i)
                    break

            elif i=='}':
                if now and now[-1]=='{':
                    del now[-1]
                else:
                    now.append(i)
                    break

            elif i==']':
                if now and now[-1]=='[':
                    del now[-1]
                else:
                    now.append(i)
                    break
        tmp=list_s[0]
        del list_s[0]
        list_s.append(tmp)
        if not now:
            count+=1

    return count