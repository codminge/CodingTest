def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(signs), 1):
        if signs[i] == True:
            answer = answer + absolutes[i]
        else:
            answer = answer + -absolutes[i]
    return answer