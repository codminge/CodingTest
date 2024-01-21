def solution(slice, n):
    if int(n/slice) == n/slice:
        return n/slice
    else:
        return int(n/slice) + 1