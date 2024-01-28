def solution(n):
    answer = []
    for i in range(0, n, 1):
        temp = []
        for j in range(0, n, 1):
            if j == i:
                temp.append(1)
            else:
                temp.append(0)
        answer.append(temp)
    return answer