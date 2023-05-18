#def solution(n):
#    a = []
#    n = str(n)
#    for i in n:
#        a.append(int(i))
#    a = sorted(a, reverse=True)
#    b=''
#    for i in a:
#        b += str(i)
#    return int(b)

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))