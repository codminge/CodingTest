def solution(left, right):
    answer = 0
    sumEven = 0
    num = []
    temp = []
    
    for i in range(left, right+1, 1):
        num.append(i)
    
    for i in num:
        answer = 0
        for j in range(1, right+1, 1):
            if i / j == int(i / j):
                answer = answer + 1
        temp.append(answer)
        
    for i in range(0, len(temp), 1):
        if temp[i] % 2 == 0:
            sumEven = sumEven + num[i]
        else:
            sumEven = sumEven - num[i]
            
    return sumEven