def solution(arr):
    answer = []
    for i in range(0, 11, 1):
        if len(arr) != 2**i and len(arr) < 2**i:
            for j in range(0, 2**i-len(arr), 1):
                answer.append(0)
            break
        elif len(arr) == 2**i:
            return arr
    arr.extend(answer)
    return arr