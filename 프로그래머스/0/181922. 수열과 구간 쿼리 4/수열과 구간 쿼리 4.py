def solution(arr, queries):
    for i in range(0, len(queries), 1):
        s, e, k = queries[i]
        for j in range(s, e-s+1, 1):
            if j/k == int(j/k):
                arr[j] = arr[j] + 1
    return arr