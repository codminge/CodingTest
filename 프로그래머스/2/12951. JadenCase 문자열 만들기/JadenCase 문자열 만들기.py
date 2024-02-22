def solution(s):
    answer = ''
    s = s.lower()
    sList = list(s)
    
    for i in range(0, len(sList), 1):
        if sList[i-1] == ' ':
            sList[i] = sList[i].upper()
        else:
            sList[0] = sList[0].upper()
        if sList[0].isdigit():
            answer = answer + sList[i]
        else:
            answer = answer + sList[i]

    return answer