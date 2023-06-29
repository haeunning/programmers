def solution(num_list):
    a = []
    b = []
    for i in range(len(num_list)):
        if i % 2 ==0:
            a.append(num_list[i])
        else:
            b.append(num_list[i])
    return max(sum(a),sum(b))