def solution(arr, n):
    idx = len(arr)
    if idx % 2 == 1:
        for i in range(0, idx, 2):
            arr[i] = arr[i] + n
    else:
        for i in range(1, idx, 2):
            arr[i] = arr[i] + n
    return arr