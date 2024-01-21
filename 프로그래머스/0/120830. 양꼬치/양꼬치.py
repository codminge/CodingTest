def solution(n, k):
    answer = 0
    service = int(n / 10)
    if service >= 1:
        answer = n * 12000 + (k-service) * 2000
    else:
        answer = n * 12000 + k * 2000
    return answer