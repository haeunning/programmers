from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        piro = k
        duns = 0
        for need, spend in p:
            if piro >= need:
                piro -= spend
                duns += 1
        answer = max(answer, duns)
    return answer