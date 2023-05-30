def solution(a, b):
    num = 0
    for i in range(len(a)):
        num += a[i]*b[i]
    return num