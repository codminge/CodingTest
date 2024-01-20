def solution(num_list):
    answer = 0
    sumEven = 0
    sumOdd = 0
    idx = len(num_list)
    for i in range(0, idx, 2):
        sumOdd = sumOdd + num_list[i]
    for j in range(1, idx, 2):
        sumEven = sumEven + num_list[j]
    if sumOdd >= sumEven:
        answer = sumOdd
    elif sumOdd <= sumEven:
        answer = sumEven
    return answer