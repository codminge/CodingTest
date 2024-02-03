import math

def solution(n):
    sqrtN = math.sqrt(n)
    print(sqrtN == int(sqrtN))
    if sqrtN == int(sqrtN):
        return (sqrtN+1)**2
    return -1