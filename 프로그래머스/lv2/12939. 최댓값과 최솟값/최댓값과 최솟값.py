def solution(s):
    ss = s.split(' ')
    a = []
    b = []
    for i in ss:
        a.append(int(i))
    b.append(max(a))
    b.append(min(a))
    b = sorted(b)
    return ' '.join(map(str,b))