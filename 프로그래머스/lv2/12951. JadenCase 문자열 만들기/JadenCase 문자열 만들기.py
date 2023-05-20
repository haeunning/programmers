def solution(s):
    s = s.split(' ')
    a = []
    for i in range(len(s)):
        a.append(s[i].capitalize())
    return ' '.join(map(str,a))