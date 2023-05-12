def solution(n):
    a = list(str(n))
    a.reverse()
    return list(map(int,a))

#def digit_reverse(n):
#    return list(map(int, list(str(n))[::-1]))
#reverse 기억 안나면 [::-1]