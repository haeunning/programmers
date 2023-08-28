n,m = map(int,input().split())
num = list(map(int,input().split()))
num = sorted(num, reverse=True)
print(num[m-1])