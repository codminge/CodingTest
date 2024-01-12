def solution(my_string, overwrite_string, s):
    leno = len(overwrite_string)
    a = my_string[0:s]
    changePart = my_string[s:leno+s]
    b = my_string[leno+s:]
    answer = a + overwrite_string + b
    return answer