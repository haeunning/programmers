import math
def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    gcd = math.gcd(a,b)
    aa = a/gcd
    bb = b/gcd
    return [aa,bb]