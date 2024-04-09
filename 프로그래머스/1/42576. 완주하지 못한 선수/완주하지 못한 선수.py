# from collections import Counter
# def solution(participant, completion):
#     count_p = Counter(participant)
#     count_c = Counter(completion)
#     for i in count_p:
#         if count_p[i] > count_c[i]:
#             return i

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]