def solution(my_string, num1, num2):
    answer = []
    temp = []
    idx = len(my_string)
    for i in range(0, idx, 1):
        if i == num1:
            answer.append(my_string[num2])
        elif i == num2:
            answer.append(my_string[num1])
        else:
            answer.append(my_string[i])
    answer = ''.join(answer)
    return answer