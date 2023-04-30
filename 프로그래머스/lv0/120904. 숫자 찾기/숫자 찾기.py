def solution(num, k):
    k = str(k)
    if str(num).find(k) != -1:
        return str(num).find(k)+1
    else:
        return str(num).find(k)