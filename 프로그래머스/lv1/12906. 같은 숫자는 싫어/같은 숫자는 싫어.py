def solution(arr):
    a = []
    for i in range(len(arr)):
        if i == 0:
            a.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                a.append(arr[i])
    return a