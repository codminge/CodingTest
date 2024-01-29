def solution(myStr):
    answer = []
    temp = ""
    for i in myStr:
        if i == "a" or i == "b" or i == "c":
            answer.append(temp)
            temp = ""
        else:
            temp = temp + i
    answer.append(temp)
    answer = ' '.join(answer).split()
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer