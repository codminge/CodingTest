def solution(s):
    answer = 0
    sList = s.split()
    idx = len(sList)
    for i in range(0, idx, 1):
        if sList[i] == "Z":
            answer = answer - int(sList[i-1])
        else:
            answer = answer + int(sList[i])
    return answer