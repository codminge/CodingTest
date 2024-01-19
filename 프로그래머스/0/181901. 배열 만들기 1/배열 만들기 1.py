def solution(n, k):
    answer = []
    for i in range(1, int(n / k) + 1, 1):
        answer.append(k * i)
    return answer