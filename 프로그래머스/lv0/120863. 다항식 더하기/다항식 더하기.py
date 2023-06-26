def solution(polynomial):
    poly = polynomial.replace(' ','').split('+')
    a = []
    b = []
    for i in poly:
        if 'x' in i:
            a.append(i)
        else:
            i = int(i)
            b.append(i)
    x = []
    for i in a:
        i = i.replace('x','')
        if i == '':
            i = '1'
        i = int(i)
        x.append(i)
    if sum(x) ==1 and sum(b) !=0:
        return 'x'+' + '+str(sum(b))
    elif sum(x) >1 and sum(b) !=0:
        return str(sum(x))+'x'+' + '+str(sum(b))
    elif sum(x) ==0 and sum(b) !=0:
        return str(sum(b))
    elif sum(x) > 1 and sum(b) ==0:
        return str(sum(x))+'x'
    elif sum(x) == 1 and sum(b) ==0:
        return 'x'
    else:
        return 0