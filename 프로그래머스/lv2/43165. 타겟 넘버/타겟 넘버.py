def solution(numbers, target):
    leaves = [0]
    count = 0
    for num in numbers:
        temp = []
        #자손노드
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)
        leaves = temp
        
    for i in leaves:
        if i == target:
            count += 1
    return count