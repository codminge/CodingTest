def solution(numbers, n):
    idx = len(numbers)
    sumNum = 0
    for i in range(0, idx+1, 1):
        sumNum = sumNum + numbers[i]
        if sumNum > n:
            break
    return sumNum