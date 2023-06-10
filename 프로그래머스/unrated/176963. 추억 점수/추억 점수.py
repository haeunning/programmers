def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        a = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                a += yearning[name.index(photo[i][j])]
        answer.append(a)
    return answer