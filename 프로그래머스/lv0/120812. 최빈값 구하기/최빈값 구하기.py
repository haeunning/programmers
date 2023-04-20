def solution(array):
    num = list(set(array))
    num_count = []
    for n in num:
        num_count.append(array.count(n))
    if num_count.count(max(num_count))>1:
        answer = -1
    else:
        answer = num[num_count.index(max(num_count))] 
    return answer