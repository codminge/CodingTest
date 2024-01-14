def solution(n):
    numOdd = 0
    numEven = 0
    if n % 2 == 1:
        for i in range(1, n+2, 2):
            numOdd = numOdd + i
            answer = numOdd
    else:
        for i in range(2, n+2, 2):
            numEven = numEven + i**2
            answer = numEven
    return answer