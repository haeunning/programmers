def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    n = []
    for i in num:
        if i not in numbers:
            n.append(i)
    return sum(n)