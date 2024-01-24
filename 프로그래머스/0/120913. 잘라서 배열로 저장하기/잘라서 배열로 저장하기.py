def solution(my_str, n):
    answer = []
    idx = len(my_str)
    for i in range(0, idx, n):
        answer.append(my_str[i:i+n])
    return answer