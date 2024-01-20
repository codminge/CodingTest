def solution(myString, pat):
    answer = 0
    temp = list(myString)
    myString = myString.replace("A", "B")
    myString = list(myString)
    idx = len(myString)
    
    for i in range(0, idx, 1):
        if temp[i] == "B":
            myString[i] = "A"        
    myString = ''.join(myString)
    
    if pat in myString:
        answer = 1
    return answer