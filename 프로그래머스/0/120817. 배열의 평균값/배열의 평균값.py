def solution(numbers):
    answer = 0
    sumNumbers = 0
    idx = len(numbers)
    for i in numbers:
        sumNumbers = sumNumbers + i
    answer = sumNumbers/idx
    return answer