def solution(numbers):
    numbers.sort()
    idx = len(numbers)
    return numbers[idx-2] * numbers[idx-1]