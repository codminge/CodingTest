def solution(myString):
    for i in myString:
        if ord(i) < ord("l"):
            print(i)
            myString = myString.replace(i, "l")
    return myString