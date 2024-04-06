n = int(input())
sentence = list(input() for i in range(n))

tot = 0
for word in sentence:
    no = [word[0]]
    nono = []
    for w in range(1,len(word)):
        if word[w] != word[w-1]:
            no.append(word[w])
    for n in range(len(no)):
        if no[n] not in nono:
            nono.append(no[n])
    if no == nono:
        tot += 1
print(tot)