def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(0, len(s), 1):
        for j in range(0, len(s[i]), 1):
            if j % 2 == 0:
                answer = answer + s[i][j].upper()
            else:
                answer = answer + s[i][j].lower()
        if i != len(s)-1:
            answer = answer + " "
    return answer