def solution(myString, pat):
    p = ''
    for i in pat:
        if i=='A':
            p += 'B'
        else:
            p += 'A'
    if p in myString:
        return 1
    else:
        return 0