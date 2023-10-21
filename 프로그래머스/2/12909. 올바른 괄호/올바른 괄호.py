def solution(s):
    temp=[]
    for i in s:
        if i=='(':
            temp.append(i)
        else:
            if temp==[]:
                return False
            else:
                temp.pop()
    return temp==[]