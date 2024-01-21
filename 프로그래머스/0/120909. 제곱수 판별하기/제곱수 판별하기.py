def solution(n):
    answer = 0
    sumN = 0
    for i in range(1, n+1, 1):
        if int((n)/i) == (n)/i:
            sumN = sumN + 1
            if sumN % 2 == 1:
                answer = 1
            else:
                answer = 2
    return answer