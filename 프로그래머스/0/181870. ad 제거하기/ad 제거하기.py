def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i:
            answer = answer + [i]
    return answer