def solution(arr1, arr2):
    answer = []
    temp = []
    for i in range(0, len(arr1), 1):
        temp = []
        for j in range(0, len(arr1[0]), 1):
            temp = temp + [arr1[i][j] + arr2[i][j]]
        answer.append(temp)
    return answer