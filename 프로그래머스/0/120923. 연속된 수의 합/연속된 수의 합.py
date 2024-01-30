def solution(num, total):
    answer = []
    if num % 2 == 1:
        midNum = total // num
        answer = calculation(num, midNum)
    else:
        midNum = (total // num) + 1 
        answer = calculation(num, midNum)
    return sorted(answer)

def calculation(num, midNum):
    answer = []
    temp = midNum
    for i in range(0, num, 1):
        if i > num//2:
            temp = temp + 1
            answer.append(temp)
            temp = answer[i]
        if i < num//2:
            temp = temp - 1
            answer.append(temp)
            temp = answer[i]
        if i == num//2:
            temp = temp + 1
            answer.append(midNum)
            temp = answer[i]
    return answer