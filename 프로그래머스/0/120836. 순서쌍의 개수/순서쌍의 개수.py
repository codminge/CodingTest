def solution(n):
    answer = 0
    for i in range(1, n+1, 1):
        if int(n/i) == n/i:
            answer = answer + 1
    return answer