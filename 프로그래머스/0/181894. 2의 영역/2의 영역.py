def solution(arr):
    answer = []
    temp = []
    for i in range(0, len(arr), 1):
        if arr[i] == 2:
            temp.append(i)
    tempLen = len(temp)
    if tempLen == 0:
        answer.append(-1)
    elif tempLen == 1:
        answer.append(2)
    elif tempLen == 2:
        answer.extend(arr[temp[0]:temp[1]+1])
    else:
        answer.extend(arr[temp[0]:temp[tempLen-1]+1])
    return answer