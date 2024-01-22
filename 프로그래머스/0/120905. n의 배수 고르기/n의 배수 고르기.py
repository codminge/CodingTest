def solution(n, numlist):
    answer = []
    for i in numlist:
        if i/n == int(i/n):
            answer.append(i)
    return answer