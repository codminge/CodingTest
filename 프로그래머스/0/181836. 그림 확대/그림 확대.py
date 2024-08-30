import numpy as np

def solution(picture, k):
    answer = []
    temp = ""
    for i in picture:
        for j in i:
            temp = temp + (j*k)
            if len(temp) == len(i)*k:
                z = 0
                while k != z:
                    answer.append(temp)
                    z = z + 1
                temp = ""
    return answer