def solution(array, n):
    array.sort()
    a = []
    for i in range(len(array)):
        a.append(abs(n-array[i]))
    b=a.index(min(a))
    return array[b]