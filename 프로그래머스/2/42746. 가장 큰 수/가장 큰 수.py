def solution(numbers):
    num = [str(i) for i in numbers]
    num.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(num)))