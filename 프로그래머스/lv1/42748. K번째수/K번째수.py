def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        point = commands[i][2]
        if start != end:
            new = array[start-1:end]
            new_s = sorted(new)
            answer.append(new_s[point-1])
        else:
            answer.append(array[start-1])
    return answer