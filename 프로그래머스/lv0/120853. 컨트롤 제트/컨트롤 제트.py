def solution(s):
    a = []
    for num in s.split(' '):
        try:
            a.append(int(num))
        except:
            a.pop()
    return sum(a)