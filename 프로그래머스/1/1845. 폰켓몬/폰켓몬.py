def solution(nums):
    nums_set = set(nums)
    if len(nums)//2 > len(nums_set):
        answer = len(nums_set)
    else:
        answer = len(nums)//2
    return answer