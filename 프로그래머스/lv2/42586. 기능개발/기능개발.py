def solution(progresses, speeds):
    answer = []
    days = 0
    role = 0
    while len(progresses)>0:
        if (progresses[0]+days*speeds[0])>=100:
            progresses.pop(0)
            speeds.pop(0)
            role+=1
        else:
            if role>0:
                answer.append(role)
                role=0
            else:
                days+=1
    answer.append(role)
    return answer