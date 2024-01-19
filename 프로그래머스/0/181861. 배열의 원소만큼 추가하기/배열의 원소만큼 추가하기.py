def solution(arr):
    answer = []
    for i in arr:
        num = 0
        while i != num:
            answer.append(i)
            num = num + 1
            continue
    return answer