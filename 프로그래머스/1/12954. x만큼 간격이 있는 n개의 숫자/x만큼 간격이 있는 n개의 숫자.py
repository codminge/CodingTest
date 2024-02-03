def solution(x, n):
    answer = []
    temp = x
    for i in range(0, n, 1):
        answer.append(temp)
        temp = temp + x 
    return answer