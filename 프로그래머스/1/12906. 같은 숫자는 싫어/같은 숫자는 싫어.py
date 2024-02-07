def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr), 1):
        if arr[i-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer