s=input()
tot=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        tot.add(s[i:j+1])
print(len(tot))