def solution(number):
    answer = 0
    sumNumber = 0
    for i in number:
        sumNumber = sumNumber + int(i)
    answer = sumNumber % 9
    return answer