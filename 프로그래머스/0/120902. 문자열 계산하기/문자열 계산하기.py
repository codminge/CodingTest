def solution(my_string):
    my_string = my_string.split()
    print(my_string)
    idx = len(my_string)
    answer = int(my_string[0])
    for i in range(0, idx, 1):
        if my_string[i] == "+":
            answer = answer + int(my_string[i+1])
        elif my_string[i] == "-":
            answer = answer - int(my_string[i+1])
    return answer