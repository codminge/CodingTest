def solution(myString, pat):
    answer = ''
    temp = 0
    for i in range(0, len(myString), 1):
        if pat == myString[i:len(pat)+i]:
            temp = i
    return myString[:len(pat)+temp]