def solution(age):
    answer = ''
    age = str(age)
    for i in age:
        for j, letter in enumerate(["a", "b", "c", "d", "e", 
                                "f", "g", "h", "i", "j"]):
            if str(j) == i:
                answer = answer + letter
    return answer