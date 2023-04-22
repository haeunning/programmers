def solution(sides):
    if sum(sides) <= max(sides)*2:
        answer = 2
    else:
        answer = 1
    return answer