import math

def solution(n):
    sqrtN = math.sqrt(n)
    if sqrtN == int(sqrtN):
        return (sqrtN+1)**2
    return -1