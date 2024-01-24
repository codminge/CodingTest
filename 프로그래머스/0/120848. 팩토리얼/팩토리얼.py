def solution(n):
    answer = 0
    temp = 1
    for i in range(1, 11, 1):
        temp = temp * i
        if n >= temp:
            answer = i
    return answer