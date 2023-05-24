def solution(arr):
    if len(arr) > 1:
        arr.pop(arr.index(min(arr)))
    else:
        arr = [-1]
    return arr