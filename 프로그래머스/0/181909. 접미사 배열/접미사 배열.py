def solution(my_string):
    answer = []
    idx = len(my_string)
    count = idx-1
    for i in range(idx-1, -1, -1):
        answer.append(my_string[count:idx:])
        count = count-1
    return sorted(answer)