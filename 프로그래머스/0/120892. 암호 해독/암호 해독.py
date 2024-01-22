def solution(cipher, code):
    answer = ''
    count = 0
    for i in cipher:
        count = count + 1
        if count / code == int(count / code):
            answer = answer + i
    return answer