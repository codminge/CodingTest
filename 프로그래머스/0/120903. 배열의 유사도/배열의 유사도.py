def solution(s1, s2):
    answer = 0
    for i in s1:
        for y in s2:
            if i == y:
                answer = answer + 1
    return answer