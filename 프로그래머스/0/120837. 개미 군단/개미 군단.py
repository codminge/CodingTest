def solution(hp):
    answer = 0
    temp = 0
    if hp % 5 / 3 == int(hp % 5 / 3):
        temp = int(hp / 5) + (hp % 5 / 3)
        answer = temp
    elif hp / 5 == int(hp / 5):
        temp = int(hp / 5)
        answer = temp
    elif hp % 5 >= 4:
        temp = int(hp / 5) + int(hp % 5 / 3) + (hp % 5 - 3)
        answer = temp
    else:
        temp = int(hp / 5) + (hp % 5)
        answer = temp
    return answer