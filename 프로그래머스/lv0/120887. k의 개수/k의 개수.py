def solution(i, j, k):
    num = 0
    for a in range(i,j+1):
        lst_str = list(str(a))
        if str(k) in lst_str:
            num += lst_str.count(str(k))
    return num