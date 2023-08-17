grade = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}

i = 1
tot_score = 0
tot = 0

while i < 21 :
    name, score, rank = input().split()
    if rank == 'P': pass
    else:
        tot_score += float(score)
        tot += float(score)*grade[rank]
    i += 1
    
print(tot/tot_score)