def solution(arr):
    answer = []
    idx = len(arr)
    for i in range(0, idx, 1):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i] / 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = arr[i] * 2
    return arr