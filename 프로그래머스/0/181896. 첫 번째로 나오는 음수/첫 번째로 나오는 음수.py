def solution(num_list):
    answer = 0
    idx = len(num_list)
    for i in range (0, idx, 1):
        if num_list[i] < 0:
            answer = i
            break
        else:
            answer = -1
    return answer