def solution(str_list, ex):
    answer = ''
    idx = len(str_list)
    for i in range(0, idx, 1):
        if ex not in str_list[i]:
            answer = answer + ''.join(str_list[i])
    return answer