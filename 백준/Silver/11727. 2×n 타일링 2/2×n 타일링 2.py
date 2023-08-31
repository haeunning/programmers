from sys import stdin

n = int(stdin.readline())
tile_list = [1, 1]
for i in range(2, n + 1):
    tile_list.append(tile_list[i - 1] + 2*tile_list[i - 2])

print(tile_list[n] % 10007)