def solution(arr, k):
    answer = []
    for i in range(0, len(arr), 1):
        if arr[i] not in answer:
            answer.append(arr[i])
        if len(answer) == k:
            break
    while len(answer) < k:
        answer.append(-1)
        if len(answer) == k:
            break
    return answer