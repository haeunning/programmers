from collections import deque

def solution(prices):
    prices = deque(prices)
    count = []
    while prices:
        i = prices.popleft()
        c = 0
        for j in prices:
            c += 1
            if i > j:
                break
        count.append(c)
    return count