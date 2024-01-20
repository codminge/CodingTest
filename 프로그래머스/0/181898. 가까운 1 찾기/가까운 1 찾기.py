def solution(arr, idx):
    answer = -1
    arr_len = len(arr)
    for i in range(0, arr_len, 1):
        if i >= idx and arr[i] == 1:
            answer = i
            break
    return answer