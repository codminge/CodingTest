def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if k < int(i[int(s):int(s)+int(l)]):
            answer.append(int(i[int(s):int(s)+int(l)]))
    return answer