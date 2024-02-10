def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    tempList = []
    
    for a, b in queries:
        if a != 0:
            my_string = my_string[0:a] + my_string[b:a-1:-1] + my_string[b+1:]
        else:
            temp = my_string[0]
            tempList = my_string[b:a:-1]
            tempList.append(temp)
            tempList = tempList + my_string[b+1:]
            my_string = tempList
    return ''.join(my_string)