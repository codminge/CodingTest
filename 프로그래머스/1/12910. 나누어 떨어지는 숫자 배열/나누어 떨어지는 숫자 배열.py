def solution(arr, divisor):
    answer = []
    for i in arr:
        if i / divisor == int(i / divisor):
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)