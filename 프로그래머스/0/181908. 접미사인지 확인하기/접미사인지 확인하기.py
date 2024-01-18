def solution(my_string, is_suffix):
    answer = 0
    idx = len(my_string)
    for i in range(0, idx, 1):
        if is_suffix == my_string[-i:]:
            answer = 1
            break
        else:
            answer = 0
    return answer