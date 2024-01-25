def solution(my_string, m, c):
    answer = ''
    myList = []
    for i in range(0, len(my_string), m):
        myList = myList + [my_string[i:i+m]]
    for i in myList:
        answer = answer + i[c-1]
    return answer