def solution(my_string, is_prefix):
    answer = 0
    idx = len(my_string)
    print(idx)
    for i in range(1, idx+1, 1):
        if is_prefix == my_string[:i]:
            return 1
    return answer