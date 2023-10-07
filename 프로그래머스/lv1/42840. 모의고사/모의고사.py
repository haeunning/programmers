def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    aa=0
    bb=0
    cc=0
    best = []
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            aa+=1
        if answers[i] == b[i%8]:
            bb+=1
        if answers[i] == c[i%10]:
            cc+=1
    if aa == max(aa,bb,cc):
        best.append(1)
    if bb == max(aa,bb,cc):
        best.append(2)
    if cc == max(aa,bb,cc):
        best.append(3)
    return best