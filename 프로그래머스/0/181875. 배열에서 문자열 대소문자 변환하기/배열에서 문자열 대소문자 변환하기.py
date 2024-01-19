def solution(strArr):
    answer = []
    idx = len(strArr)
    for i in range(0, idx, 1):
        if i % 2 == 1:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer