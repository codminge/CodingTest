def solution(numbers, direction):
    answer = []
    idx = len(numbers)
    if direction == "right":
        answer.append(numbers[idx-1])
        for i in range(0, idx-1, 1):
            answer.append(numbers[i])
    if direction == "left":
        for i in range(1, idx, 1):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer