def solution(my_string, index_list):
    answer = ''
    result = []
    for i in my_string:
        result.append(i)
    for y in index_list:
        answer = answer + result[y]
    return answer