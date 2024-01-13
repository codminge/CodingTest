def solution(a, b):
    sum1 = int(str(a) + str(b))
    sum2 = int(str(b) + str(a))
    if sum1 >= sum2:
        answer = sum1
    else:
        answer = sum2
    return answer