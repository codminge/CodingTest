def solution(num, k):
    answer = -1
    numList = list(str(num))
    idx = len(numList)
    for i in range(0, idx, 1):
        if numList[i] == str(k):
            answer = i+1
            break
    return answer