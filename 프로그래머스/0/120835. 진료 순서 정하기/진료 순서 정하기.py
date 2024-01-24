def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    for i in emergency:
        for j in temp:
            if i == j:
                answer.append(temp.index(i)+1)
    return answer