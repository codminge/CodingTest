def solution(i, j, k):
    answer = 0
    for n in range(i, j+1, 1):
        answer = answer + str(n).count(str(k))
    return answer