def solution(arr, flag):
    answer = []
    for i in range(0, len(arr), 1):
        if flag[i] == True:
            for j in range(0, 2*arr[i], 1):
                answer.append(arr[i])
        else:
            for j in range(0, arr[i], 1):
                answer.pop()
    return answer