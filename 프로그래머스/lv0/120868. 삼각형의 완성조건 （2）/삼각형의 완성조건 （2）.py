def solution(sides):
    a = [] #max 기준
    b = [] #max 되기
    for i in range(max(sides)+1):
        if i+min(sides) > max(sides):
            a.append(i)
    for j in range(max(sides)+1,sum(sides)+1):
        if j < sum(sides):
            b.append(j)
    return len(a)+len(b)