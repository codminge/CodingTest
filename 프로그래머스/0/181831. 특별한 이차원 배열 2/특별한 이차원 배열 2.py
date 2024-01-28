def solution(arr):
    answer = 1
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer