def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            n = n / i
            if i in answer:
                continue
            answer.append(i)
        else:
            i = i + 1
    return answer