def solution(numLog):
    answer = ''
    idx = len(numLog)
    for i in range(0, idx-1, 1):
        if numLog[i+1] - numLog[i] == 1:
            answer += "w"
        elif numLog[i+1] - numLog[i] == -1:
            answer += "s"
        elif numLog[i+1] - numLog[i] == 10:
            answer += "d"
        elif numLog[i+1] - numLog[i] == -10:
            answer += "a"
    return answer