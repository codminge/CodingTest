def solution(numbers):
    answer = 0
    temp = []
    idx = len(numbers)
    for i in range(0, idx-1, 1):
        for j in range(i+1, idx, 1):
            temp.append(numbers[i]*numbers[j])
    answer = max(temp)
    return answer