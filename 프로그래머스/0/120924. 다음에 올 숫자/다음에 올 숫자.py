def solution(common):
    answer = 0
    num1 = common[0]
    num2 = common[1]
    num3 = common[2]
    d = 0
    r = 0
    idx = len(common)
    
    if num2 - num1 == num3 - num2:
        d = num2 - num1
        answer = common[idx-1] + d 
    else:
        r = num2 / num1
        answer = common[idx-1] * r 
    
    return answer