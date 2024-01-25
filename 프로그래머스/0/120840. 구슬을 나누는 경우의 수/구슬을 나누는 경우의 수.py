def solution(balls, share):
    return fac(balls)/(fac(balls-share)*fac(share))

def fac(num):
    facNum = 1
    for i in range(1, num+1, 1):
        facNum = facNum * i
    return facNum