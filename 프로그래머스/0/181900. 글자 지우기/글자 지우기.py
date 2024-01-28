def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for i in indices:
        del my_string[i]
        my_string.insert(i, "")
    return ''.join(my_string)