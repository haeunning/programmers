def solution(box, n):
    a = []
    for i in range(len(box)):
        a.append(box[i]//n)
    return a[0]*a[1]*a[2]