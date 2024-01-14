def solution(a, d, included):
    num = 0
    idx = len(included)
    for i in range(0, idx, 1):
        if included[i] == True:
            print(i)
            num = num + arithmeticSequence(a, d, i)
    return num

def arithmeticSequence(a, d, idx):
    return a + (idx * d)
    