def solution(n):
    hap = 0
    yack = []
    for i in range(2,n+1):
        for j in range(1,i+1):
            if i%j==0:
                yack.append(i)
        if yack.count(i)>2:
            hap += 1
    return hap