def solution(myString):
    myString = myString.split("x")
    answer = ' '.join(myString).split()
    return sorted(answer)