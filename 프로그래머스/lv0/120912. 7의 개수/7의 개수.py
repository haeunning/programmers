def solution(array):
    a=0
    for i in array:
        if str(i).count("7") > 0:
            a += str(i).count("7")
    return a