def solution(start, end_num):
    answer = []
    num = start - end_num
    for i in range(0, num + 1, 1):
        answer.append(start - i)
    return answer