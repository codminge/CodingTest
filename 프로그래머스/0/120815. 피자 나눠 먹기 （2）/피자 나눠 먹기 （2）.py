def solution(n):
    answer = 0
    for i in range(1, 17, 1):
        if (n * i / 6) == int(n * i / 6):
            answer = n * i / 6
            break
    return answer