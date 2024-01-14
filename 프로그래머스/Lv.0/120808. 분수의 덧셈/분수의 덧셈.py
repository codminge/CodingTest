import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = 0
    if denom1 == denom2:
        numer = numer1 + numer2
        denom = denom1
    else:
        denom = denom1 * denom2
        numer = (numer1 * denom2) + (numer2 * denom1)
    gcd = math.gcd(denom, numer)
    if gcd != 1:
        numer, denom = divisionGCD(numer, denom, gcd)
    answer.append(numer)
    answer.append(denom)
    return answer

def divisionGCD(numer, denom, gcd):
    numer = numer / gcd
    denom = denom / gcd
    return numer, denom

