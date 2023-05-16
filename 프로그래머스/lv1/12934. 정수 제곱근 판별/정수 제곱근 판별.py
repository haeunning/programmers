import math as m
def solution(n):
    if m.sqrt(n) == int(m.sqrt(n)):
        return (m.sqrt(n)+1)**2
    else:
        return -1