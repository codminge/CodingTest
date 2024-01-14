def solution(num_list):
    answer = 0
    sumList = 0
    multipleList = 1
    idx = len(num_list)
    for i in range(0, idx, 1):
        multipleList = multipleList * num_list[i]
        sumList = sumList + num_list[i]
    sumSquareList = (sumList) ** 2
    if multipleList > sumSquareList:
        answer = 0
    else:
        answer = 1
    return answer