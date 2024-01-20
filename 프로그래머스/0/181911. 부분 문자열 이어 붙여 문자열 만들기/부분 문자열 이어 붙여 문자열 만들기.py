def solution(my_strings, parts):
    answer = ''
    idx = len(my_strings)
    for i in range(0, idx, 1):
        answer = answer + (my_strings[i][parts[i][0]:parts[i][1]+1:1])
    return answer