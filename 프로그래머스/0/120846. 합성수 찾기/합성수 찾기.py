def solution(n):
    answer = 0
    for i in range(1, n+1, 1):
        for j in range(1, i, 1):
            if (i / j) == int(i / j) and j != 1 and j != i:
                answer = answer + 1
                break
    return answer