def solution(id_pw, db):
    answer = ''
    for a,b in db:
        if a == id_pw[0]:
            if b == id_pw[1]:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
    return answer