def solution(clothes):
    hash = {}
    for name, kind in clothes:
        if kind in hash.keys():
            hash[kind] += [name]
        else:
            hash[kind] = [name]
    tot = 1
    for key, value in hash.items():
        tot *= (len(value)+1)
    return tot-1