def solution(num, total):
    answer = []
    if num % 2 == 1:
        midNum = total // num
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
    else:
        midNum = (total // num) + 1 
        temp = midNum
        for j in range(0, num, 1):
            if j > num//2:
                temp = temp + 1
                answer.append(temp)
                temp = answer[j]
            if j < num//2:
                temp = temp - 1
                answer.append(temp)
                temp = answer[j]
            if j == num//2:
                temp = temp + 1
                answer.append(midNum)
                temp = answer[j]
    return sorted(answer)