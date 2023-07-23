m = [i for i in range(1,31)]

for _ in range(28):
    data = int(input())
    m.remove(data)
    
print(min(m))
print(max(m))