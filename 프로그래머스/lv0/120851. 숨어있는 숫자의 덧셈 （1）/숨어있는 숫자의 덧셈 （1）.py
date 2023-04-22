def solution(my_string):
    num = [0,1,2,3,4,5,6,7,8,9]
    num = list(map(str,num))
    a = []
    for i in my_string:
        if i in num:
            a.append(i)
    return sum(map(int,a))