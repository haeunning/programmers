#장군5,병정3,일1
def solution(hp):
    return hp//5 + (hp-hp//5*5)//3 +  (hp-hp//5*5)%3