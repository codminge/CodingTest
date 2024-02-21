def solution(s):
    answer = ''
    sList = s.split(' ')
    maxsList = int(sList[0])
    minsList = int(sList[0])
    
    for i in sList:
        if maxsList < int(i):
            maxsList = int(i)
        if minsList > int(i):
            minsList = int(i)
        
    answer = str(minsList) + " " + str(maxsList)
    
    return answer