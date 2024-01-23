def solution(n):
    answer = []
    for i in range(1, n+1, 1):
        if n/i == int(n/i):
            answer.append(i)
    answer.sort()
    return answer