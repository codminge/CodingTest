def solution(t, p):
    answer = 0
    pLen = len(p)
    for i in range(0, len(t)+1, 1):
        if len(t[i:i+pLen]) == pLen and int(t[i:i+pLen]) <= int(p):
            answer = answer + 1
    return answer