def solution(n):
    answer = 0
    answer = sorted(str(n))
    answer.reverse()
    return int("".join(answer))