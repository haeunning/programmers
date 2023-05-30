def solution(n):
    i=0
    answer = ''
    while i<n:
        if i%2 == 1:
            answer += '박'
        else:
            answer += '수'
        i += 1
    return answer