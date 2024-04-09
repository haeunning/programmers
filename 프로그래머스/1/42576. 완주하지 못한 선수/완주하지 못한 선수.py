from collections import Counter
def solution(participant, completion):
    count_p = Counter(participant)
    count_c = Counter(completion)
    for i in count_p:
        if count_p[i] > count_c[i]:
            return i