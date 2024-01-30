def solution(M, N):
    count = 0
    while N != 1:
        count = count + M
        N = N - 1
    while M != 1:
        count = count + 1
        M = M - 1
    return count