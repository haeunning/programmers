n = int(input())
word = [input() for _ in range(n)]
word = list(set(word))
word.sort(key=lambda x: (len(x),x))
for i in word:
    print(i)