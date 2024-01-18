def solution(num_list, n):
    answer = []
    idx = len(num_list)
    for i in range(0, idx, 1):
        if i < n:
            answer.append(num_list[i])
    return answer