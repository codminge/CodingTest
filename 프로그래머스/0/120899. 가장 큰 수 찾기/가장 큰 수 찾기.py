def solution(array):
    answer = []
    maxArray = max(array)
    for idx, ch in enumerate(array):
        if ch == maxArray:
            answer.append(ch)
            answer.append(idx)
    return answer