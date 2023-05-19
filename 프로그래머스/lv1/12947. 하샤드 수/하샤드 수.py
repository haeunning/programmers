def solution(x):
    a=[]
    for i in str(x):
        a.append(int(i))
    if x%sum(a) == 0:
        return True
    else:
        return False