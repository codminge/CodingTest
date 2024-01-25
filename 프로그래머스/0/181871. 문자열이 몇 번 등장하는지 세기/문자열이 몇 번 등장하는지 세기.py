def solution(myString, pat):
    count = 0
    patIdx = len(pat)
    for i in range(0, len(myString), 1):
        if pat in myString[i:i+patIdx]:
            count = count + 1
    return count