h, m = map(int, input().split())
m += int(input())

if m >= 60:
    h += m//60
    m = m%60
    if h >= 24:
        h -= 24
    else:
        h += m//60

print(h,m)