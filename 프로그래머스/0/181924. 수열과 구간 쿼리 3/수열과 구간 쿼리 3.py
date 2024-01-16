def solution(arr, queries):
    temp = 0
    for x, y in queries:
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    return arr