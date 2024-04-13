def solution(brown, yellow):
    answer = [0,0]
    for i in range(1,yellow+1):
        if yellow%i == 0:
            x = i
            y = yellow//i
            if x+y == brown//2-2:
                answer[0] = max(x,y)+2
                answer[1] = min(x,y)+2
                break
    return answer