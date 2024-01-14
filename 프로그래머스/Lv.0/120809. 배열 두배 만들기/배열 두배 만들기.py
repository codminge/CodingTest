def solution(numbers):
    idx = len(numbers)
    for i in range(0, idx, 1):
        numbers[i] = numbers[i] * 2
    return numbers